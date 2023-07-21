from django.db import models

""" 公共字段模型 """
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')    
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    is_delete = models.BooleanField(default=False,verbose_name='删除标记')
    class Meta:
        abstract =True
        verbose_name_plural = "公共字段模型"
        db_table = 'BaseTable'

""" 基础区域模型 """
class BaseArea(models.Model):
    pid = models.ImageField(verbose_name='上级ID')
    name = models.CharField(verbose_name='地区名',max_length=20)
    level = models.CharField(verbose_name='区域等级',max_length=20)
    class Meta:
        abstract =True
        verbose_name_plural = "区域模型"
        db_table = 'BaseAreaTable'

""" 基础验证码模型 """
class BaseVerifCode(models.Model):
    mobile = models.CharField(max_length=11,verbose_name='手机号码')
    code = models.CharField(max_length=6,verbose_name='验证码')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='生成时间')
    class Meta:
        abstract =True
        verbose_name_plural = "基础验证码模型"
        db_table = 'BaseVerifCodeTable'