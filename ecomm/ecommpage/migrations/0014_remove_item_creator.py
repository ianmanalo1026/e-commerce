# Generated by Django 3.1.7 on 2021-03-04 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommpage', '0013_auto_20210304_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='creator',
        ),
    ]
