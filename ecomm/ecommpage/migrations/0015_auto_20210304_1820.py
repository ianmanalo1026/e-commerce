# Generated by Django 3.1.7 on 2021-03-04 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommpage', '0014_remove_item_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecommpage.item'),
        ),
    ]