# Generated by Django 4.1.3 on 2022-12-06 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='getinforlowwer14',
            old_name='currentplace',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='getinforupper14',
            old_name='currentplace',
            new_name='location',
        ),
    ]
