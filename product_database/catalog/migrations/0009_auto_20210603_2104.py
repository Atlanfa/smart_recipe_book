# Generated by Django 3.2 on 2021-06-03 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0008_auto_20210601_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='who_added',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_added_to_price_type', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='who_added',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_added_to_product_type', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='store',
            name='who_added',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_added_to_store_type', to=settings.AUTH_USER_MODEL),
        ),
    ]
