# Generated by Django 3.2 on 2021-07-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_dish_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='recipe',
            field=models.CharField(help_text='Enter recipe', max_length=100000),
        ),
    ]