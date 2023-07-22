""" 自定义 多字段 用户登录认证类"""
from django.contrib.auth.backends import ModelBackend
from drfdemo.models import User
from django.db.models import Q
from rest_framework import serializers


class MyBackends(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username) | Q(email=username))
        except:
            raise serializers.ValidationError({'error': '未找到该用户!！'})
        else:
            if user.check_password(password):
                return user
            else:
                raise serializers.ValidationError({'error': '密码错误！'})