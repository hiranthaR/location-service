# Generated by Django 3.0.3 on 2020-02-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20200217_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='latitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locations',
            name='longitute',
            field=models.FloatField(default=6.0),
            preserve_default=False,
        ),
    ]