# Generated by Django 4.2.3 on 2023-07-20 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drfdemo', '0012_naturalperson_user_lealperson_employee_department'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LealPerson',
            new_name='LegalPerson',
        ),
    ]
