import json
from django import forms
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app import models
from app.utils.bootstrap import BootStrapModelForm
from app.utils.pagination import Pagination

# 任务 TaskModelForm
class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "detail": forms.TextInput
            #"detail": forms.Textarea
        }

# 任务列表
def task_list(request):
    queryset = models.Task.objects.all().order_by('-id')
    page_object = Pagination(request,queryset,page_size=5)
    form = TaskModelForm()

    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分页的完整数据
        "page_string": page_object.html()       # 生成页码
    }
    return render(request, "task_list.html", context)

# 免除发出POST请求时的token验证
@csrf_exempt
def task_ajax(request):
    #print(request.GET)
    print(request.POST)
    data_dict = {"status": True, "data": [11, 22, 33, 44]}
    #return HttpResponse(json.dumps(data_dict))
    #return HttpResponse(json.dumps(request.GET))
    return HttpResponse(json.dumps(request.POST))

# 任务 task_add
@csrf_exempt
def task_add(request):
    # 校验数据
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    
    data_dict = {"status": False,"error": form.errors}
    return HttpResponse(json.dumps(data_dict))
    
