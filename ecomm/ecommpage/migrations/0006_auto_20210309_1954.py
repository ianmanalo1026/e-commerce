# Generated by Django 3.1.7 on 2021-03-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommpage', '0005_auto_20210309_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='order',
            name='reference_number',
            field=models.CharField(blank=True, default='9980434149', max_length=10, null=True),
        ),
    ]