# Generated by Django 3.0.7 on 2020-11-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humpy_food_app', '0013_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
