# Generated by Django 4.1.10 on 2023-09-23 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_filesupload_uploadedby_filesupload_uploadedon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesupload',
            name='uploadedby',
        ),
        migrations.RemoveField(
            model_name='filesupload',
            name='uploadedon',
        ),
    ]
