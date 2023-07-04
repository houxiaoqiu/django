"""
URL configuration for djsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.views.static import serve
from django.urls import path, re_path
from django.conf import settings
from django.contrib import admin

from app.views import home,department,user,partner,admin,account,task,work,chart,file,vue,register


urlpatterns = [
    # 配置 media 用户数据目录
    re_path(r'^media/(?P<path>.*)$', serve, {'ducument_root': settings.MEDIA_ROOT}, name='media'),

    # 首页
    path('index/',home.index),
    
    # 用户注册
    path('register/',register.register),

    # 部门管理
    path('department/list/',department.department_list),
    path('department/add/',department.department_add),
    path('department/delete/',department.department_delete),
    path('department/<int:nid>/edit/',department.department_edit),
    path('department/multi/',department.department_multi),

    #用户管理
    path('user/list/',user.user_list),
    path('user/add/',user.user_add),
    path('user/<int:nid>/delete/',user.user_delete),
    path('user/<int:nid>/edit/',user.user_edit),
    path('user/model/form/add/',user.user_model_form_add),
    
    # 客商管理
    path('partner/list/',partner.partner_list),
    path('partner/add/',partner.partner_add),
    path('partner/<int:nid>/delete/',partner.partner_delete),
    path('partner/<int:nid>/edit/',partner.partner_edit),
    
    # 管理员
    path('admin/list/',admin.admin_list),
    path('admin/add/',admin.admin_add),
    path('admin/<int:nid>/delete/',admin.admin_delete),
    path('admin/<int:nid>/edit/',admin.admin_edit),
    path('admin/<int:nid>/reset/',admin.admin_reset),
    
    # 登录/注销
    path('login/',account.login),
    path('logout/',account.logout),
    path('image/code/',account.image_code),
    
    # 任务管理
    path('task/list/',task.task_list),
    path('task/ajax/',task.task_ajax),
    path('task/add/',task.task_add),

    # 工单管理
    path('work/list/',work.work_order_list),
    path('work/add/',work.work_order_add),
    path('work/delete/',work.work_order_delete),
    path('work/edit/',work.work_order_edit),
    path('work/edit/save/',work.work_order_edit_save),
    path('work/cancel/<int:pk>',work.work_order_cancel,name="work_order_cancel"),    # 撤单

    # 图表
    path('chart/list/',chart.chart_list),
    path('chart/bar/',chart.chart_bar),

    # 文件管理
    path('file/upload/list/',file.upload_list),
    path('file/upload/form/',file.upload_form),
    path('file/upload/modelform/',file.upload_modelform),
    path('file/upload/employee/',file.upload_employee),

    # vue
    path('vue/test01/',vue.vue_test01),

]
