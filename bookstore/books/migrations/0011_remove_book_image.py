# Generated by Django 4.0 on 2022-02-14 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]
