JWT
    pip install djangorestframework-simplejwt

路由
    根路由 
        path('drfdemo/',include("drfdemo.urls")),  # 子路由
    子路由
        from rest_framework_simplejwt.views import TokenObtainPairView
        urlpatterns = [
            path('login/',TokenObtainPairView.as_view())
        ]
    url
        http://127.0.0.1:8000/drfdemo/login/

创建超级管理员
    python manage.py createsuperuser
注册接口
    描述：用户注册接口
    请求URL：/drfdemo/register
    请求方式：POST
    Body请求参数
        name,必选，sring，昵称
        email,必选，sring，邮箱
        password,必选，sring，密码
        password_comfirmation,必选，sring，确认密码
登录接口
    描述：用户登录接口
    请求URL：/drfdemo/login
    请求方式：POST
    body请求参数
        email,必选，sring，邮箱
        pwssword,必选，sring，密码
    返回参数
        status_code,必选，int，状态码
        message,必选，sring，结果
        data,必选，string，{refresh_token,access_token,username,email,token_type}