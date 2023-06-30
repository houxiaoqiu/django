import datetime
from django.db import models

# ActiveBaseModel
class ActiveBaseModel(models.Model):
    active = models.SmallIntegerField(
        verbose_name="状态",
        default=1,
        choices=(
            (1,"激活"),
            (2,"删除")
        )
    )
    class Meta:
        abstract = True

# 部门
class Department(models.Model):
    title = models.CharField(verbose_name='部门',max_length=32)
    def __str__(self):
        return self.title
    
# 用户
class User(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄',default=18)
    balance = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2, default=0)
    create_time = models.DateField(verbose_name='建档时间')
    gender_choices = ((1,"男"),(2,"女"),)
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices,default=2)
    # # 部门级联删除
    depart = models.ForeignKey(verbose_name='部门',to="Department",to_field="id",on_delete=models.CASCADE)
    # # 部门级联置空
    # depart = models.ForeignKey(verbose_name='部门',to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=None)
    def __str__(self):
        return self.name
    
# 用户信息
class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄',default=18)
    balance = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='建档时间')
    gender_choices = ((1,"男"),(2,"女"),)
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices,default=2)
    # # 部门级联删除
    #depart = models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)
    # # 部门级联置空
    department = models.ForeignKey(verbose_name='部门',to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=20)
    def __str__(self):
        return self.name

# 人员
class Employee(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=16)
    age = models.IntegerField(verbose_name='年龄',default=18)
    gender_choices = ((1,"男"),(2,"女"),)
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices,default=1)
    img = models.FileField(verbose_name='图片',max_length=128,default=None,upload_to='employee/')
    photo = models.FileField(verbose_name='头像',max_length=128,default=None,upload_to='employee/')
    create_time = models.DateField(verbose_name='建档时间',auto_now_add=True)
    # # 部门级联删除
    #depart = models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)
    # # 部门级联置空
    department = models.ForeignKey(verbose_name='部门',to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=20)

# 客商 business partner（客户&供应商）customers and merchants
class Partner(models.Model):
    number = models.CharField(verbose_name='客户代码',max_length=32,unique=True)
    name = models.CharField(verbose_name='客户名称',max_length=32,unique=True)
    short_name = models.CharField(verbose_name='客户简称',max_length=16,unique=True)
    telephone_number = models.CharField(verbose_name='电话号码',max_length=32)
    category_choices = ((1,"客户"),(2,"供应商"))
    category = models.SmallIntegerField(verbose_name='类别',choices=category_choices,default=1)
    region_choices = (
        (1,"华北"),(2,"东北"),(3,"华东"),(4,"华中"),(5,"华南"),(6,"西南"),(7,"西北"),(8,"港澳台")
        )
    region = models.SmallIntegerField(verbose_name='区域',choices=region_choices,default=1)
    status_choices = ((1,"启用"),(2,"停用"))
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choices,default=1)
    def __str__(self):
        return self.name
    
# 物料
class Material(models.Model):
    number = models.CharField(verbose_name='物料编码',max_length=32,unique=True)
    code = models.CharField(verbose_name='物料代码',max_length=32)
    name = models.CharField(verbose_name='物料名称',max_length=32)
    uom = models.ForeignKey(verbose_name='计量单位',to="UomGroup",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=None)
    def __str__(self):
        return self.number
    
# 基本计量单位
class BasicUom(models.Model):
    code = models.CharField(verbose_name='基本计量单位代码',max_length=32,unique=True)
    name  = models.CharField(verbose_name='基本计量单位',max_length=32)
# 计量单位组
class UomGroup(models.Model):
    uom_group_code = models.CharField(verbose_name='计量单位组代码',max_length=32,unique=True)
    name  = models.CharField(verbose_name='计量单位组',max_length=32,unique=True)
    level_choices = ((1,"主计量"),(2,"辅助计量"),)
    level = models.SmallIntegerField(verbose_name='计量类别',choices=level_choices,default=1)
    conversion_rate = models.DecimalField(verbose_name='换算率',max_digits=10,decimal_places=2, default=1)
    basic_uom = models.ForeignKey(verbose_name='计量单位',to="BasicUom",to_field="id",on_delete=models.CASCADE) 
    
# 生产订单
class ProductionOrder(models.Model):
    number = models.CharField(verbose_name='生产订单号',max_length=32,unique=True)
    create_date = models.DateField(verbose_name='单据日期')
    expect_date = models.DateField(verbose_name='计划完成日期')
    department = models.ForeignKey(verbose_name='生产部门',to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=None)
    customer = models.ForeignKey(verbose_name='客户',to="Partner",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=None)
    
# 生产订单明细
class ProductionOrders(models.Model):
    number = models.CharField(verbose_name='生产订单行号',max_length=16,unique=True)
    expect_date = models.DateField(verbose_name='计划完成日期')
    production_order = models.ForeignKey(verbose_name='生产订单号',to="ProductionOrder",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=None)  
    quantity = models.DecimalField(verbose_name='数量',max_digits=10,decimal_places=2, default=0)

# 管理员
class Admin(models.Model):
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    def __str__(self):
            return self.username
# 任务
class Task(models.Model):
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题",max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人",to="Admin",to_field="id", on_delete=models.CASCADE)

# 派工单 WorkOrder
class WorkOrder(models.Model):
    number = models.CharField(verbose_name='工单号',unique=True,max_length=64)
    create_date = models.DateField(verbose_name='单据日期')
    planned_start_date = models.DateField(verbose_name='计划开始日期')
    planned_completion_date = models.DateField(verbose_name='计划完工日期')
    department = models.ForeignKey(verbose_name='生产部门',to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=None)
    partner = models.ForeignKey(verbose_name='客户',to="Partner",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=None)
    material = models.ForeignKey(verbose_name='产品',to="Material",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=None)
    quantity = models.DecimalField(verbose_name='数量',max_digits=10,decimal_places=2, default=1)
    admin = models.ForeignKey(verbose_name='操作员',to="Admin",to_field="id",on_delete=models.CASCADE)
    status_choices = (
        (1, "开立"),
        (2, "开启"),
        (3, "执行"),
        (4, "停滞"),
        (5, "完工"),
        (6, "关闭"),
        (7, "撤销")
    )
    status = models.SmallIntegerField(verbose_name="状态",choices=status_choices,default=1)




