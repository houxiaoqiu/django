# Generated by Django 4.2.3 on 2023-07-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfdemo', '0003_alter_student_age_alter_student_class_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '学生', 'verbose_name_plural': '学生'},
        ),
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.TextField(max_length=1000, null=True, verbose_name='个性签名'),
        ),
    ]
