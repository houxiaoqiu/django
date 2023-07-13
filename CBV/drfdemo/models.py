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