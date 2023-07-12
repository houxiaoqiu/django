# Generated by Django 4.2.3 on 2023-07-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('gender', models.BooleanField(default=1, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('class_number', models.CharField(max_length=5, verbose_name='班级编号')),
            ],
            options={
                'db_table': 'tb_student',
            },
        ),
    ]
