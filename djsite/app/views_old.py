from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import Department,UserInfo
from app import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from app.utils.pagination import Pagination
from app.utils.bootstrap import BootStrapModelForm

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用Django")

def orm(request):
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="采购部")
    # Department.objects.create(title="运营部")

    # UserInfo.objects.create(name="张三",password="123456")
    # UserInfo.objects.create(name="李四",password="123456",age=19)
    # UserInfo.objects.create(name="王五",password="123456",age=20)
    # UserInfo.objects.create(name="赵六",password="123456",age=21)

    #Department.objects.filter(title="采购部").delete()

    #data_list = UserInfo.objects.all()
    #for obj in data_list:
    #    print(obj.id,obj.name,obj.password,obj.age)
    
    #UserInfo.objects.filter(id=1).update(password="999")

    return HttpResponse("添加数据成功")

# 部门列表
def department_list(request):
    queryset = models.Department.objects.all()
    return render(request,'department_list.html',{'queryset': queryset})

# 部门新增
def department_add(request):
    if request.method == 'GET':
        return render(request,'department_add.html')
    else:
        title = request.POST.get('title')
        models.Department.objects.create(title=title)
        return redirect("/department/list/")

# 部门删除
def department_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/department/list/")

# 部门编辑
def department_edit(request,nid):
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request,'department_edit.html',{"row_object":row_object})
    else:
        title = request.POST.get("title")
        models.Department.objects.filter(id=nid).update(title=title)
        return redirect("/department/list/")

# 用户信息列表
def user_info_list(request):
    data_list = UserInfo.objects.all()
    return render(request,"user_list.html",{"data_list": data_list})

# 用户列表
def user_list(request):
    queryset = models.User.objects.all()
    page_object = Pagination(request,queryset,page_size=10)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request,'user_list.html',context)

# 用户新增
def user_add(request):
    if request.method == "GET":
        return render(request,'user_add.html')
    else:
        name = request.POST.get("name")
        password = request.POST.get("password")
        age = request.POST.get("age")
        UserInfo.objects.create(name=name,password=password,age=age)
        return redirect("/user/list/")

# 用户新增 UserModelForm
class UserModelForm(BootStrapModelForm):
    password = forms.CharField(min_length=6,label="密码")
    class Meta:
        model = models.User
        fields = ["name","password","gender","age","balance","depart","create_time"]

# 用户新增             
def user_model_form_add(request):
    if request.method == "GET":   
        form = UserModelForm()
        return render(request,'user_model_form_add.html',{"form": form})
    else:
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('/user/list/')
        else:
            #print(form.errors)
            return render(request,'user_model_form_add.html',{"form": form})

# 用户删除
def user_delete(request,nid):
    models.User.objects.filter(id=nid).delete()
    return redirect("/user/list/")

# 用户编辑
def user_edit(request,nid):
    row_object = models.User.objects.filter(id=nid).first()
    if request.method == 'GET':   
        form = UserModelForm(instance=row_object)
        return render(request,'user_edit.html',{'form': form})
    else:
        form = UserModelForm(data=request.POST,instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/user/list/")
        else:
            return render(request,'user_edit.html',{"form": form})
        
# 客商列表
def partner_list(request):
    ## 搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data
    ## 列表
    queryset = models.Partner.objects.filter(**data_dict).order_by("category")
    page_object = Pagination(request,queryset)
    ## 分页
    page_string = page_object.html()
    ## 结果  
    context =  {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_string
    } 
    return render(request,'partner_list.html',context)

# 客商 PartnerModelForm
class PartnerModelForm(BootStrapModelForm):
    telephone_number = forms.CharField(
        label="电话号码",
        validators=[RegexValidator(r'^1[3-9]\d{9}$','电话号码错误')]
    )
    class Meta:
        model = models.Partner
        #fields = ["number","name","short_name","telephone_number","category","region","status"]
        fields = "__all__"
    # 验证
    def clean_name(self):
        txt_name = self.cleaned_data["name"]
        exists = models.Partner.objects.filter(name=txt_name).exists()
        if exists:
            raise ValidationError("客商名称已存在")
        else:
            return txt_name

# 客商 PartnerEditModelForm
class PartnerEditModelForm(BootStrapModelForm):
    telephone_number = forms.CharField(
        label="电话号码",
        validators=[RegexValidator(r'^1[3-9]\d{9}$','电话号码错误')]
    )
    class Meta:
        model = models.Partner
        #fields = ["number","name","short_name","telephone_number","category","region","status"]
        fields = "__all__"
    # 验证
    def clean_name(self):
        txt_name = self.cleaned_data["name"]
        exists = models.Partner.objects.exclude(id=self.instance.pk).filter(name=txt_name).exists()
        if exists:
            raise ValidationError("客商名称已存在")
        else:
            return txt_name

# 客商新增
def partner_add(request):
    if request.method == "GET":   
        form = PartnerModelForm()
        return render(request,'partner_add.html',{"form": form})
    else:
        form = PartnerModelForm(data=request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('/partner/list/')
        else:
            #print(form.errors)
            return render(request,'partner_add.html',{"form": form})

# 客商编辑
def partner_edit(request,nid):
    row_object = models.Partner.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PartnerEditModelForm(instance=row_object)
        return render(request,'partner_edit.html',{'form': form})
    else:
        form = PartnerEditModelForm(data=request.POST,instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/partner/list")
        else:
            return render(request,'partner_edit.html',{"form": form})

# 客商删除
def partner_delete(request,nid):
    models.Partner.objects.filter(id=nid).delete()
    return redirect("/partner/list")


