# Generated by Django 5.1.1 on 2024-10-26 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_storeproductcount_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeproductcount',
            name='price',
        ),
    ]
