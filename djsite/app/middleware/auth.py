from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
# from web import models

# 
class AuthMiddleware(MiddlewareMixin):
    """ 登录验证中间件 """
    def process_request(self,request):
        # 设置非验证页面
        if request.path_info in ["/login/","/image/code/","/index/"]:
            return
        
        """ 新版本 """
        # 获取用户信息
        # user_id = request.session.get('user_id',0)
        # user_object = models.User.objects.filter(id=user_id).first()
        # request.tracer = user_object
            
        # # 如果用户已登录则继续，否则返回登录页面
        # if not request.tracer:
        #     return redirect('login')
        
        """ 原版本 """
        # 获取用户session信息
        info_dict = request.session.get("info")
        if info_dict:
            return
        # 如果用户已登录
        return redirect('/login/')

