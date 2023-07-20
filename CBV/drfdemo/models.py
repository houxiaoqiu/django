from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100,verbose_name="姓名")
    gender = models.BooleanField(default=1,verbose_name="性别")
    age = models.IntegerField(default=18,verbose_name="年龄")
    class_number = models.CharField(max_length=5,default='1',verbose_name="班级编号")
    description = models.TextField(max_length=1024,default='1',verbose_name="个性签名")

    class Meta:
        db_table = "tb_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name="书籍名称")
    price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="价格")
    pub_date = models.DateField(verbose_name="出版日期")
    bread = models.IntegerField(verbose_name="阅读量")
    bcomment = models.IntegerField(verbose_name="评论量")
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE, verbose_name='出版商')
    authors = models.ManyToManyField("Author",verbose_name="作者")
    class Meta:
        db_table = "tb_book"
        verbose_name = "书籍"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
    
class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name="出版商")
    email = models.EmailField(verbose_name="出版商邮箱")
    class Meta:
        db_table = "tb_publish"
        verbose_name = "出版商"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者")
    age = models.IntegerField(verbose_name="年龄")
    
    class Meta:
        db_table = "tb_author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name
            
    def __str__(self):
        return self.name
    
class Contacts(models.Model):
    Leal = 'LE'
    Natural = 'NA'
    Partner = 'PA'
    Unrelated = "UN"
    IdentityCard = "IC"
    EnterpriseCode = "EC"
    name = models.CharField(max_length=64,verbose_name="名称")
    feature_choices = (
        (Leal,'法人'),
        (Natural,'自然人'),
    )
    feature = models.CharField(
        max_length=2,
        choices=feature_choices,
        default=Natural,
        verbose_name="特征")
    realationship_choices = (
        (Partner,'合作伙伴'),
        (Unrelated,'无关'),)
    realationship = models.CharField(
        max_length=2,
        choices=realationship_choices,
        default=Partner,
        verbose_name="关系")
    id_type_choices = (
        (IdentityCard,'身份证'),
        (EnterpriseCode,'企业代码证'),)
    id_type = models.CharField(
        max_length=2,
        choices=id_type_choices, 
        verbose_name="证件类型")
    id_number = models.CharField(max_length=32,verbose_name="证件号")
    

    class Meta:
        abstract = True
        verbose_name = "联系人"
        verbose_name_plural = verbose_name

class NaturalPerson(Contacts):
    gender = models.CharField(max_length=16,verbose_name="性别")
    birthday = models.DateField(verbose_name="生日")
    telephone = models.CharField(max_length=16,verbose_name="电话号码")
    email = models.CharField(max_length=64,verbose_name="电子邮箱")

    class Meta:
        verbose_name="人员"
        verbose_name_plural = verbose_name

class LegalPerson(Contacts):
    short_name = models.CharField(max_length=16,verbose_name="简称")
    address = models.CharField(max_length=128,verbose_name="地址")
    representative = models.ForeignKey(
        NaturalPerson, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="法人代表")

    class Meta:
        verbose_name="法人单位"
        verbose_name_plural = verbose_name

class User(models.Model):
    app = models.CharField(max_length=32,verbose_name="应用系统")
    account = models.CharField(max_length=16,verbose_name="帐号")
    password = models.CharField(max_length=16,verbose_name="密码")
    person = models.ForeignKey(
        NaturalPerson,
        on_delete=models.CASCADE, 
        verbose_name="用户")

    class Meta:
        verbose_name="用户"
        verbose_name_plural = verbose_name

class Employee(models.Model):
    person = models.OneToOneField(
        NaturalPerson, 
        on_delete=models.CASCADE, 
        verbose_name="雇员")
    employer = models.ForeignKey(
        LegalPerson, 
        on_delete=models.CASCADE, 
        verbose_name="雇主")

    class Meta:
        verbose_name="雇员"
        verbose_name_plural = verbose_name

class Department(models.Model):
    name = models.CharField(max_length=32,verbose_name="部门名称")
    leal_person = models.ForeignKey(
        LegalPerson,
        on_delete=models.CASCADE, 
        verbose_name="法人单位")
    parent_name = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        verbose_name="上级部门")
    class Meta:
        verbose_name="部门"
        verbose_name_plural = verbose_name