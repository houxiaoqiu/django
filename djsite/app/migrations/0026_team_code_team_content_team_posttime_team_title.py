# Generated by Django 4.2.3 on 2023-07-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_attendancerecord_equitpment_inspectionitem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='code',
            field=models.CharField(default=1, max_length=16, unique=True, verbose_name='班组代码'),
        ),
        migrations.AddField(
            model_name='team',
            name='content',
            field=models.TextField(default=None, verbose_name='班组说明'),
        ),
        migrations.AddField(
            model_name='team',
            name='posttime',
            field=models.DateTimeField(auto_now=True, verbose_name='记录时间'),
        ),
        migrations.AddField(
            model_name='team',
            name='title',
            field=models.CharField(default=None, max_length=32, verbose_name='班组名称'),
        ),
    ]
