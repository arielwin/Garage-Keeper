# Generated by Django 5.1.1 on 2024-09-04 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealership_app', '0003_alter_car_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
    ]
