# Generated by Django 3.2 on 2021-07-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_alter_dish_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='products',
            field=models.ManyToManyField(to='catalog.ProductAmount'),
        ),
    ]
