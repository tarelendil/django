# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170104_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=300)),
                ('official_price', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('in_cart_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='ImageModel',
            new_name='Image',
        ),
        migrations.DeleteModel(
            name='ProductModel',
        ),
        migrations.AlterField(
            model_name='image',
            name='related_to_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]