from django.shortcuts import redirect, render
from app import models
from app.utils.pagination import Pagination
from app.utils.form import PartnerEditModelForm, PartnerModelForm

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

