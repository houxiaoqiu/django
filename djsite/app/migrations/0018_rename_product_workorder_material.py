# Generated by Django 4.2.2 on 2023-06-26 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_workorder_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workorder',
            old_name='Product',
            new_name='material',
        ),
    ]