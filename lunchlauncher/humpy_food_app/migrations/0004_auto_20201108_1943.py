# Generated by Django 3.0.7 on 2020-11-08 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('humpy_food_app', '0003_auto_20201108_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setprofile',
            old_name='username',
            new_name='user',
        ),
    ]
