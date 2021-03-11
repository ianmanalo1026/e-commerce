# Generated by Django 3.1.7 on 2021-03-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommpage', '0009_auto_20210311_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='reference_number',
            field=models.CharField(blank=True, default='2299377651', max_length=10, null=True, unique=True),
        ),
    ]