# Generated by Django 4.2.2 on 2023-06-26 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='detail',
            field=models.TextField(verbose_name='详细信息'),
        ),
    ]