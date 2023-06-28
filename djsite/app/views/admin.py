from django.shortcuts import render,redirect

from app import models
from app.utils.pagination import Pagination

from django import forms
from app.utils.bootstrap import BootStrapModelForm
from django.core.exceptions import ValidationError
from app.utils.encrypt import md5

# 管理员列表
def admin_list(request):
    # 搜索条件
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data
    # 获取搜索（过滤）后的记录
    queryset = models.Admin.objects.filter(**data_dict)
    page_object = Pagination(request,queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'search_data': search_data
    }
    return render(request,'admin_list.html',context)

# 管理员新增
def admin_add(request):
    title = "新增管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(
            request,
            'change.html',
            {
                "form": form, 
                "title": title
            }
        )
        
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request,'change.html',{'form': form, 'title': title})

# 管理员 AdminModelForm
class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["username","password","confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
    
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致，请重新输入！")
        return confirm
    
# 管理员 AdminEditModelForm
class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ["username"]

# 管理员 AdminResetModelForm
class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["password"]

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("不可与以前密码一致！")
        return md5(pwd)
    
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致，请重新输入！")
        return confirm
    
# 管理员编辑
def admin_edit(request,nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        # return render(request,'error.html',{"msg": "数据不存在"})
        return redirect('/admin/list/')
    title = "编辑管理员"

    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request,'change.html',{"form": form,"title": title})
    
    form = AdminEditModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request,'change.html',{"form": form,"title": title})

# 管理员删除
def admin_delete(request,nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')

# 管理员重置密码
def admin_reset(request,nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')
    
    title = "重置密码 [ {} ]".format(row_object.username) 

    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request,'change.html', {'form': form ,'title': title})
    
    form = AdminResetModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request,'change.html', {'form': form ,'title': title})
        