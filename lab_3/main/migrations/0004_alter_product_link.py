# Generated by Django 5.0.6 on 2024-05-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.CharField(default='', max_length=200),
        ),
    ]
