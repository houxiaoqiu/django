from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect


# 中间件 AuthMiddleware
class AuthMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # 设置非验证页面
        if request.path_info in ["/login/","/image/code/"]:
            return
        
        # 获取用户session信息
        info_dict = request.session.get("info")
        if info_dict:
            return
        return redirect('/login/')

