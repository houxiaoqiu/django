# Generated by Django 4.2.2 on 2023-06-28 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_employee_depart_remove_employee_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.FileField(default=None, max_length=128, upload_to='employee/', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='img',
            field=models.CharField(default=None, max_length=128, verbose_name='图片'),
        ),
    ]