# Generated by Django 3.1.7 on 2021-03-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommpage', '0002_auto_20210311_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reference_number',
            field=models.CharField(blank=True, default='9860067695', max_length=10, null=True),
        ),
    ]
