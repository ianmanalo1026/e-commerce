# Generated by Django 3.1.7 on 2021-03-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]