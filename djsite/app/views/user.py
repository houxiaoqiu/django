from django.shortcuts import redirect, render
from app import models
from app.utils.form import UserModelForm
from app.utils.pagination import Pagination
from rest_framework import viewsets

def user_list(request):
    """ 用户列表 """
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
        
