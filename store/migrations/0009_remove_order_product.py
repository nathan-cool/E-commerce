# Generated by Django 5.0.2 on 2024-09-16 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
