# Generated by Django 3.1.7 on 2021-03-01 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('since', models.DateTimeField(auto_now_add=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('street_address', models.CharField(max_length=300)),
                ('provice', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
