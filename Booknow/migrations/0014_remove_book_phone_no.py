# Generated by Django 4.1.7 on 2023-04-08 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booknow', '0013_alter_book_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Phone_no',
        ),
    ]
