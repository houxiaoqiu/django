# Generated by Django 4.2.2 on 2023-06-26 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_workorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='create_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.admin', verbose_name='操作员'),
        ),
    ]