# Generated by Django 3.1.6 on 2021-04-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210428_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='air_data',
            name='distance_travelled',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
