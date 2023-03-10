# Generated by Django 4.1.3 on 2022-12-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_topic_product_host_product_image_product_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Exterior_color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='Transmission',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='engine_type',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='fuel_type',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='interior_color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='used_or_new',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='vehicle_id',
            field=models.CharField(max_length=50),
        ),
    ]
