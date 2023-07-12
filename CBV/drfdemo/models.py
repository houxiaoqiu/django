from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100,verbose_name="姓名")
    gender = models.BooleanField(default=1,verbose_name="性别")
    age = models.IntegerField(null=True,verbose_name="年龄")
    class_number = models.CharField(max_length=5,null=True,verbose_name="班级编号")

    class Meta:
        db_table = "tb_student"

class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name="书名")
    price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="价格")
    pub_date = models.DateField(verbose_name="出版日期")
    bread = models.IntegerField(verbose_name="阅读量")
    bcomment = models.IntegerField(verbose_name="评论量")
    publish = models.ForeignKey("Publish",on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title

class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name="出版商")
    email = models.EmailField(verbose_name="出版商邮箱")

    def __str__(self):
        return self.name
