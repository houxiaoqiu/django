# Generated by Django 4.2.2 on 2023-07-12 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drfdemo', '0010_author_alter_book_publish_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfdemo.publish', verbose_name='出版商'),
        ),
    ]
