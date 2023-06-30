Django
    安装：pip install django
    创建项目：django-admin startproject <mysite>    # 任意目录
    创建app：python manage.py startapp <app>        # django项目目录
    注册app：settings.py                            # django项目的项目子目录
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'app.apps.AppConfig'
        ]
    配置app：
        静态目录：static        # app目录
        模板目录：templates     # app目录    
    启动django服务：python manage.py runserver 
MySQL
    Mysql第三方模块：pip install mysqlclient
    创建数据库
        Create database testdb default charset utf8 collate utf8_general_ci;
    配置数据库连接：settings.py                # django项目的项目子目录
    查询表结构：DESCRIBE 表名;
    数据
        insert into app_user (name,password,age,balance,create_time,gender,depart_id) 
        values('张三','123456',19,1000,'2023-6-21',1,1),
        ('李四','123456',20,2000,'2023-6-21',2,2),
        ('王五','123456',21,3000,'2023-6-21',2,3);

        insert into app_partner (number,name,shot_name,telephone_number,category,region,status)
        values('001','客户1','1客户','123456789',1,1,1),
        ('002','客户2','2客户','123456789',2,2,2),
        ('003','客户3','3客户','123456789',1,3,1);

ORM
    数据迁移命令
        site> python manage.py makemigrations
        site> python manage.py migrate  

编程
    project\
        manage.py
        site\
            setting.py
            urls.py
        app\
            views.py
            templates\
            static\     # css,js,应用设计图片
        media\      # 用户上传的数据文件，需要事前配置：urls.py 

    启用 media 目录配置
        (1)urls.py 配置文件
            from django.views.static import serve
            from django.urls import path, re_path
            from django.conf import settings
            urlpatterns = [
                # 配置 media 用户数据目录
                re_path(r'^media/(?P<path>.*)$', serve, {'ducument_root': settings.MEDIA_ROOT}, name='media'),
                ...,
            ]
        （2）setting.py 配置文件
            import os
            MEDIA_ROOT = os.pth.join(BASE_DIR, "media")
            MEDIA_URL = "/media/"

模型 Models
    继承：
        抽象模型继承 abstract model
        多表模型继承 multi-table inheritance
        代理模型继承 proxy model

HTML模板
    母板：
        ...
        {% block <content> %}
        {% endblock %}
        ...
    从母板继承
        {% extends 'layout.html' %}

        {% block content %}
            ......
        {% endblock %}

Django组件
    Form 组件
        views.py:
            class MyForm(Form):
                user = forms.CharFiled(widget=forms.Input)
                pwd = forms.CharFiled(widget=forms.Input)
                email = forms.CharFiled(widget=forms.Input)
            def user_add(request):
                if request == "GET":
                    form = MyForm()
                    return render(request,'user_add.html',{"form":form})

        user_add.html:
            <form method="post">
                {{ form.user }}
                {{ form.pwd }}
                {{ form.email }}
                <!-- <input type="text" placeholder="姓名" name="user" /> -->
            </form>
            或
            <form method="post">
                {% for field in form %}
                    {{ field }}
                {% endfor %}
                <!-- <input type="text" placeholder="姓名" name="user" /> -->
            </form>
    ModelForm 组件
        models.py:
            name = models.CharField(verbose_name='姓名',max_length=16)
            password = models.CharField(verbose_name='密码',max_length=64)
            email = models.CharField(verbose_name='邮箱',default=blank)

        views.py:
            class MyForm(ModelForm):
                class Meta:
                    model = User
                    fields = ["name","password","email"]
            def user_add(request):
                if request == "GET":
                    form = MyForm()
                    return render(request,'user_add.html',{"form":form})

        user_add.html:
            <form method="post">
                {% for field in form %}
                    {{ field }}
                {% endfor %}
                <!-- <input type="text" placeholder="姓名" name="user" /> -->
            </form>
操作符
    数字：
        ~.filter(id=12)     # 等于12
        ~.filter(id_gt=12)  # 大于12
        ~.filter(id_gte=12) # 大于等于12
        ~.filter(id_lt=12)  # 小于12
        ~.filter(id_lte=12) # 小于等于12
    字符：
        ~.filter(mobile__startswith="139")      # 以"139"开头
        ~.filter(mobile__endswith="000")        # 以"000"结尾
        ~.filter(mobile__contains="417")        # 包含"417"字符串

时间插件
    {% load static %}
    {% block css %}
        <link rel="stylesheet" 
            href="{% static 'plugins/bootstrap-datepicker/css/bootstrap-datepicker.min.css' %}">
    {% endblock %}

    {% block js %}
        <script 
            src="{% static 'plugins/bootstrap-datepicker/js/bootstrap-datepicker.min.js' %}">
        </script>
        <script 
            src="{% static 'plugins/bootstrap-datepicker/js/locales/bootstrap-datepicker.zh-CN.js' %}">
        </script>

        <script>
            $(function () {
                $('#id_create_time').datepicker({
                    format: 'yyyy-mm-dd',
                    startDate: '0',
                    language: 'zh-CN',
                    autoclose: true
                });
            })
        </script>
    {% endblock %}

    自定义类 & 继承
        自定义字段插件属性:
        class BootStrapModelForm(forms.ModelForm):
            def __init__(self,*args,**kwargs):
                super().__init__(*args,**kwargs)
                for name, field in self.fields.items():
                    #if name == "depart":
                    #    continue
                    if field.widget.attrs:
                        field.widget.attrs["class"] = "form-control"
                        field.widget.attrs["placeholder"] = field.label
                    else:
                        field.widget.attrs = {
                            "class": "form-control", 
                            "placeholder": field.label
                        }
        继承:
        class UserEditModelForm(BootStrapModelForm):
            class Meta:
                model = models.User
                fields = ["name","passowrd","age"]

cookie & session
    http:无状态短链接
    响应：
        响应头部：cookie(保存在浏览器中的键值对：k1=1234546)
        响应体部
    用户登录成功：网站生成随机字符串，写到用户浏览器的cookie中，再写入到session中

用户认证（中间件）
    性质：class类 process_request/process_response
    定义中间件：
    注册中间件：site/site/settings.py:
        MIDDLEWARE = [
            ...,
            app.middleware.auth.M1,
            app.middleware.auth.M2,
        ]
    处理：
    实例：登录验证
    图片验证码：
        生成动态图片：
        定义画笔-文本：
        特殊字体文件：

Ajax
    ajax请求：
        ajax({
            url: "发送的地址"
            type: "post"
            data:{
                n1:123,
                n2:456
            },
            success:function(res){
                sonsole.log(res);
            }
        })
    事件绑定：DOM绑定/jQuery绑定

图表
    highcharts  国外
    ECharts     国内


文件操作
    读取excel文件插件：
        安装：pip install openpyxl
        导入：
            import os
            from openpyxl import load_workbook
        获取workbook对象：
            file_path = os.path.join('files','pl.xlsx')
            work_book_object = load_workbook(file_path)
        获取sheet对象：
            data_list = work_book_object.sheetnames
            print(data_list)

    Form组件
    ModalForm组件

开发模式：django + drf框架 + vue.js
    django:
    drf:
    vue:

权限管理 drf + vue 
