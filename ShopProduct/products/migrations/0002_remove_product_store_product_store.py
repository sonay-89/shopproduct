# Generated by Django 5.1.1 on 2024-10-26 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='store',
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
