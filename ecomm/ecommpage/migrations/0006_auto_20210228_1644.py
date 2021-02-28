# Generated by Django 3.1.7 on 2021-02-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommpage', '0005_merge_20210227_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('C', 'Classic'), ('CB', 'Comic Book'), ('F', 'Fantacy'), ('FC', 'Fiction'), ('E', 'Educational'), ('M', 'Motivational')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]