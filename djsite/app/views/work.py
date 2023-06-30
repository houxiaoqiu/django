import json
import random
from datetime import datetime
from django import forms
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.messages.api import get_messages

from app import models
from app.utils.bootstrap import BootStrapModelForm
from app.utils.pagination import Pagination

# 工单 WorkOrderModelForm
class WorkOrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.WorkOrder
        fields = "__all__"
        ## 排除
        exclude = ["number","admin"]

# 工单列表
def work_order_list(request):
    ## 消息读取并删除：工单撤销信息
    # messages = get_messages(request)
    # for obj in messages:
    #     print(obj.message)

    ## 列表
    queryset = models.WorkOrder.objects.all().order_by('-number')
    page_object = Pagination(request, queryset)
    form = WorkOrderModelForm()
    
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, 'work\work_order_list.html', context)

# 工单新增
@csrf_exempt
def work_order_add(request):
    ## 列表
    form = WorkOrderModelForm(data=request.POST)
    if form.is_valid():
        ## 生成工单号（日期+随机数）
        form.instance.number = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        ## 获取当前用户ID
        form.instance.admin_id = request.session["info"]["id"]
        form.save()
        return JsonResponse( {"status": True } )
    return JsonResponse( {"status": False, "error": form.errors } )

# 工单删除
def work_order_delete(request):
    cid = request.GET.get('cid')
    exists = models.WorkOrder.objects.filter(id=cid).exists
    if not exists:
        return JsonResponse({"starus": False, "error": "数据不存在,删除失败。"})
    models.WorkOrder.objects.filter(id=cid).delete()
    
    return JsonResponse({"status": True })

# 工单编辑 work_order_edit
def work_order_edit(request):
    cid = request.GET.get('cid')
    row_dict = models.WorkOrder.objects.filter(id=cid).values(
            "create_date",
            "planned_start_date",
            "planned_completion_date",
            "department",
            "partner",  
            "material",
            "quantity",
            "status",
        ).first()
    if not row_dict:
        return JsonResponse({"starus": False, "error": "数据不存在。"})
    
    result = {
        "status": True,
        "data": row_dict
    }
    return JsonResponse(result)

# 工单编辑保存 work_order_edit_save
@csrf_exempt
def work_order_edit_save(request):
    cid = request.GET.get("cid")
    row_object = models.WorkOrder.objects.filter(id=cid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "数据不存在。"})
    form = WorkOrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    
    return JsonResponse({"status": False, "error": form.errors})


# 工单撤销
def work_order_cancel(request,pk):
    # 更改订单状态 =【撤销】
    wo_object = models.WorkOrder.objects.filter(id=pk, status=1).first()
    if wo_object:
        messages.add_message(request, messages.WARNING, "工单撤销失败")
        return redirect('/work/list/')


    messages.add_message(request, messages.ERROR, "工单撤销成功")
    return redirect('/work/list/')