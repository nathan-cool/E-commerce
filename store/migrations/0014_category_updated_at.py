# Generated by Django 5.0.2 on 2024-11-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_remove_category_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]