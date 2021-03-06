# Generated by Django 3.0.7 on 2020-12-05 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humpy_food_app', '0024_auto_20201203_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.CharField(choices=[('BAD', 'BAD'), ('AVERAGE', 'AVERAGE'), ('GOOD', 'GOOD'), ('AWESOME', 'AWESOME'), ('DELICIOUS', 'DELICIOUS')], max_length=10),
        ),
        migrations.AlterField(
            model_name='setprofile',
            name='image',
            field=models.ImageField(blank=True, default='/static/images/log.png', null=True, upload_to='image/'),
        ),
    ]
