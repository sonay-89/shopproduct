# Generated by Django 5.1.1 on 2024-10-26 03:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_storeproductcount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeproductcount',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='storeproductcount',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_product_counts', to='products.product'),
        ),
    ]
