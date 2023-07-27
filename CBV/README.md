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
用户登录接口
    描述：用户登录接口
    请求URL：/drfdemo/login/
    请求方式：POST
    body请求参数
        email,必选，sring，邮箱
        pwssword,必选，sring，密码
    返回参数
        status_code,必选，int，状态码
        message,必选，sring，结果
        data,必选，json，{refresh_token,access_token,username,email,token_type}
    要求
        校验参数是否为空
        校验帐号密码是否正确
        登录成功后返回token
        支持用户名多字段登录，用户名可以使用手机号、邮箱、用户名
用户注册接口
    描述：用户注册接口
    请求URL：/drfdemo/register/
    请求方式：POST
    Body请求参数
        name,必选,string,昵称
        email,必选,string,邮箱
        password,必选,string,密卡
        password-confirmation,必选,string,确认密码
刷新token接口
    描述：刷新 jwt token 接口
    请求URL：/drfdemo/token/refresh/
    请求方式：POST
    请求参数：refresh，必选，string，refresh_token
    返回参数：access,必含，string，刷新后的token
    返回示例：
校验token接口
    描述：校验 jwt token 接口
    请求URL：/drfdemo/token/verify/
    请求方式：POST
    请求参数：token，必选，string，refresh_token
    返回参数：状态码
        200 校验通过，无响应体
        401 校验失败，无效的 token
    返回示例：
获取用户信息接口
    描述：获取用户信息接口
    请求URL：/drfdemo/users/${id}/
    请求方式：GET
    请求参数：id，必选，int，用户id
    返回参数：状态码
        200 校验通过，无响应体
        401 无权限校验失败
    返回示例：
    要求：
        获取用户信息时，要进行权限校验，需要在请求头中添加认证字段
        防止越权，每个用户只能获取自己的数据
上传更新用户头像
    描述：上传用户头像
    请求URL：/drfdemo/users/${id}/avatar/upload
    请求方式：POST
    路径参数：id，必选，int，用户id
    请求参数：avatoar,必选，image，头像文件
    返回参数：状态码
        200 上传成功
        rul
    返回示例：
    要求：
        校验参数avatar
        文件大小控制不能超过300kb
        通过返回的url可以访问图片
        防止越权，每个用户只能操作自己的数据
图片获取
    接口描述：获取上传的图片
    请求URL：/media/image/图片名称
    请求方式：GET
    视图：FileView

缓存
    python manage.py createcachetable 