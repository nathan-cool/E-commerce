# Generated by Django 5.0.2 on 2024-10-03 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_category_created_at_category_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]