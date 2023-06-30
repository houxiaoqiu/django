from django.shortcuts import redirect, render,HttpResponse
from django import forms
import os
from django.conf import settings

from app.utils.bootstrap import BootStrapForm,BootStrapModelForm
from app import models

# 文件组件 UpFrom
class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ["img"]      # 排除img字段 form-control 格式
    name = forms.CharField(label="姓名")
    age = forms.CharField(label="年龄")
    img = forms.FileField(label="头像")

# 文件上传（UpForm）
def upload_form(request):
    title = "上传组件 UpFrom"
    if request.method == "GET":
        form = UpForm()
        return render(request,'file/upload_form.html',{"form": form, "title": title})
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        img_object = form.cleaned_data.get("img")
        media_path = os.path.join("media",img_object.name)
        f = open(media_path,mode='wb')
        for chunk in img_object.chunks():
            f.write(chunk)
        f.close()
        models.Employee.objects.create(
            name = form.cleaned_data["name"],
            age = form.cleaned_data["age"],
            img = media_path
        )
        return HttpResponse("...")
    return render(request,'file/upload_form.html',{"form": form, "title": title})

# 文件组件 ModelForm
class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img','photo']
    class Meta:
        model = models.Employee
        fields = "__all__"

# 文件上传 （ModalForm）
def upload_modelform(request):
    title = "上传组件 UpModelForm"
    if request.method == "GET":
        form = UpModelForm()
        return render(request,'file/upload_modelform.html',{"form":form, "title": title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect("/file/upload/employee/")
    return render(request, 'file/upload_employee.html', {"form": form, "title":title})

# Employee 上传文件列表
def upload_employee(request):
    queryset = models.Employee.objects.all()

    return render(request,'file/upload_employee.html',{"queryset": queryset})


# 文件上传
def upload_list(request):
    if request.method == "GET":
        return render(request,'file/upload_list.html')
    
    file_object = request.FILES.get("avatar")
    # print(file_object.name)     # 文件名

    # 写入文件
    f = open(file_object.name,mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close

    return HttpResponse("...")

