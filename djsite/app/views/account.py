from django import forms
from django.http import HttpResponse
from django.shortcuts import render,redirect
from io import BytesIO

from app import models
from app.utils.bootstrap import BootStrapForm
from app.utils.encrypt import md5
from app.utils.code import check_code

# 登录 LoginForm
class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

# 登录 LoginModelForm
class LoginModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ['username','password']

# 登录 login
def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,'login.html',{'form': form})
    
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 用户输入的验证码
        user_input_code = form.cleaned_data.pop('code')
        # 生成的验证码
        code = request.session.get("image_code","")
        # 验证码：校验
        if code.upper() != user_input_code.upper():
            form.add_error("code","验证码错误")
            return render(request,'login.html',{'form': form})
        # 用户名-密码：校验
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password","用户名或密码错误")
            return render(request,'login.html',{'form': form})
        # 登录成功,生成随机字符串；写入用户浏览器cookie,再写入session中
        request.session["info"] = {
            'id': admin_object.id,
            'name': admin_object.username
        }
        # session 可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)
        
        return redirect('/admin/list/')

    return render(request,'login.html',{'form': form})

# 注销 logout
def logout(requst):
    requst.session.clear()
    return redirect('/login/')

# 图片验证码 image_code
def image_code(request):
    # 生成验证码
    img,code_string = check_code()
    # 获取验证码字符,并写入session ("image_code": "????")
    request.session['image_code'] = code_string
    # 设置session时效=60秒
    request.session.set_expiry(60)
    # 验证码缓存
    stream = BytesIO()
    img.save(stream,'png')
    # 返回请求
    return HttpResponse(stream.getvalue())