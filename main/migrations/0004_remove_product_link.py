# Generated by Django 5.0.6 on 2024-06-04 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='link',
        ),
    ]