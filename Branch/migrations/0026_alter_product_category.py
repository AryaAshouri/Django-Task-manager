# Generated by Django 4.2.3 on 2023-08-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0025_product_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
