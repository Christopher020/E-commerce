# Generated by Django 4.1.4 on 2023-01-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_product_exterior_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to='product/'),
        ),
    ]
