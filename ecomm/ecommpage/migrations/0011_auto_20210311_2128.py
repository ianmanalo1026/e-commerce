# Generated by Django 3.1.7 on 2021-03-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommpage', '0010_auto_20210311_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reference_number',
            field=models.CharField(blank=True, default='8804091740', max_length=10, null=True, unique=True),
        ),
    ]
