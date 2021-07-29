# Generated by Django 3.2 on 2021-07-28 15:10

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=mapbox_location_field.models.LocationField(map_attrs={}, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='location',
            field=mapbox_location_field.models.LocationField(map_attrs={}, null=True),
        ),
    ]