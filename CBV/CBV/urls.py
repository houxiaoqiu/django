"""
URL configuration for CBV project.

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
from django.contrib import admin
from django.urls import path,re_path,include
from rest_framework import routers

from user.views import login,LoginView
from drfdemo.views import StudentView,StudentDetailView,AuthorView,PublishView  #,PublishDetailView,AuthorDetailView

router = routers.DefaultRouter()
router.register(r'author', AuthorView)
router.register(r'publish', PublishView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('student/',StudentView.as_view()),
    re_path('student/(\d+)/',StudentDetailView.as_view()),
    path('authors/', AuthorView.as_view({ "get":"list","post":"create" })),
    #re_path('authors/(\d+)/', AuthorDetailView.as_view()),
    # path('publishes/', PublishView.as_view()),
    # re_path('publishes/(?P<pk>\d+)/', PublishDetailView.as_view()),
    path('publishes/', PublishView.as_view({ "get":"list","post":"create" })),
    re_path('publishes/(?P<pk>\d+)/', PublishView.as_view({ "get":"retrieve","put":"update","delete":"destroy" })),
    path('drfdemo/',include("drfdemo.urls")),  # 子路由
    path('app01/',include("app01.urls")),  # 子路由
    path('api/',include(router.urls))
]
