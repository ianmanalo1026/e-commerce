# Generated by Django 3.1.7 on 2021-03-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommpage', '0006_auto_20210311_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reference_number',
            field=models.CharField(blank=True, default='7016493209', max_length=10, null=True),
        ),
    ]
