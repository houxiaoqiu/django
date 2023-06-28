from django import forms
from app import models
from app.utils.bootstrap import BootStrapModelForm
from django.core.validators import RegexValidator

# 用户新增 UserModelForm
class UserModelForm(BootStrapModelForm):
    password = forms.CharField(min_length=6,label="密码")
    class Meta:
        model = models.User
        fields = ["name","password","gender","age","balance","depart","create_time"]

# 客商 PartnerModelForm
class PartnerModelForm(BootStrapModelForm):
    telephone_number = forms.CharField(
        label="电话号码",
        validators=[RegexValidator(r'^1[3-9]\d{9}$','电话号码错误')]
    )
    class Meta:
        model = models.Partner
        #fields = ["number","name","short_name","telephone_number","category","region","status"]
        fields = "__all__"
    # 验证
    def clean_name(self):
        txt_name = self.cleaned_data["name"]
        exists = models.Partner.objects.filter(name=txt_name).exists()
        if exists:
            raise forms.ValidationError("客商名称已存在")
        else:
            return txt_name

# 客商 PartnerEditModelForm
class PartnerEditModelForm(BootStrapModelForm):
    telephone_number = forms.CharField(
        label="电话号码",
        validators=[RegexValidator(r'^1[3-9]\d{9}$','电话号码错误')]
    )
    class Meta:
        model = models.Partner
        #fields = ["number","name","short_name","telephone_number","category","region","status"]
        fields = "__all__"
    # 验证
    def clean_name(self):
        txt_name = self.cleaned_data["name"]
        exists = models.Partner.objects.exclude(id=self.instance.pk).filter(name=txt_name).exists()
        if exists:
            raise forms.ValidationError("客商名称已存在")
        else:
            return txt_name
