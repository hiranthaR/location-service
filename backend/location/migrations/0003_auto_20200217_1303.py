# Generated by Django 3.0.3 on 2020-02-17 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20200217_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admindistrict',
            old_name='electoral_district_id',
            new_name='electoral_district',
        ),
        migrations.RenameField(
            model_name='gramaniladaridivision',
            old_name='polingdivision_id',
            new_name='polingdivision',
        ),
        migrations.RenameField(
            model_name='location_contacts',
            old_name='location_code',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='locations',
            old_name='gdn_id',
            new_name='gdn',
        ),
        migrations.RenameField(
            model_name='media_items',
            old_name='loc_code',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='polingdivision',
            old_name='electoral_district_id',
            new_name='electoral_district',
        ),
    ]