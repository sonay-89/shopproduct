# Generated by Django 5.1.1 on 2024-11-12 16:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
        ("store", "0002_remove_store_owner"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="storeproductcount",
            name="store",
        ),
        migrations.AlterField(
            model_name="storeproductcount",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="product_counts", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="storeproductcount",
            name="product_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="store_counts", to="products.product"
            ),
        ),
        migrations.AlterField(
            model_name="storeproductcount",
            name="store_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="product_counts", to="store.store"
            ),
        ),
    ]
