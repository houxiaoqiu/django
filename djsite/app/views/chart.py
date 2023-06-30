from django.shortcuts import render
from django.http import JsonResponse

# 图表列表
def chart_list(request):
    return render(request,'chart\chart_list.html')

# 图表  柱状图数据
def chart_bar(request):
    legend = ["张三","李四"]
    series_list = [
        {
            "name": "张三",
            "type": "bar",
            "data": [15,20,36,10,10,100]
        },
        {
            "name": "李四",
            "type": "bar",
            "data": [45,10,66,40,20,10]
        }
    ]
    x_axis = ["1月","2月","3月","4月","5月","6月","7月"]
    
    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis
        }
    }
    return JsonResponse(result)