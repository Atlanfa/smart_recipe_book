# Generated by Django 3.2 on 2021-07-29 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210728_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='kid_date_of_birth',
        ),
    ]