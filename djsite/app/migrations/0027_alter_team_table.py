# Generated by Django 4.2.3 on 2023-07-05 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_team_code_team_content_team_posttime_team_title'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='team',
            table='app_team',
        ),
    ]