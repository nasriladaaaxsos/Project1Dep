# Generated by Django 3.2.16 on 2022-12-13 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20221213_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
    ]
