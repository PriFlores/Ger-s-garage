# Generated by Django 4.0.5 on 2022-06-21 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_remove_products_category_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]