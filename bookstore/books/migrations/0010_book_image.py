# Generated by Django 4.0 on 2022-02-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_review_userid_alter_book_shortdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
