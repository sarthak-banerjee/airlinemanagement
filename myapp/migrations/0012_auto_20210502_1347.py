# Generated by Django 3.1.6 on 2021-05-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20210501_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='air_data',
            name='image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
