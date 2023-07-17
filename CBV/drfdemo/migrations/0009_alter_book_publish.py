# Generated by Django 4.2.2 on 2023-07-12 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drfdemo', '0008_alter_book_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drfdemo.publish', verbose_name='出版商'),
        ),
    ]