# Generated by Django 3.0.7 on 2020-11-09 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humpy_food_app', '0004_auto_20201108_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
