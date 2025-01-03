# Generated by Django 5.1.1 on 2024-11-06 00:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("product_name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StoreProductCount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("product_name", models.CharField(max_length=255)),
                ("count", models.PositiveIntegerField()),
                ("store_name", models.CharField(max_length=255)),
                ("owner", models.CharField(max_length=255)),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="store_product_counts_store",
                        to="store.store",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
