# Generated by Django 5.0.2 on 2024-11-15 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_product_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
    ]
