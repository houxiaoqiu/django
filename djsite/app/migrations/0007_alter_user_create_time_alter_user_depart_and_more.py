# Generated by Django 4.2.2 on 2023-06-21 20:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_employee_create_time_alter_employee_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateField(default=datetime.datetime(2023, 6, 22, 4, 0, 12, 422521), verbose_name='建档时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department', verbose_name='部门'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 22, 4, 0, 12, 423601), verbose_name='建档时间'),
        ),
    ]
