# Generated by Django 5.0.6 on 2024-05-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
