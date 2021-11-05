# Generated by Django 3.0.7 on 2020-11-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humpy_food_app', '0015_order_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='track',
            field=models.CharField(choices=[('Your Order is Accepted', 'Your Order is Accepted'), ('Your Order start Cooking', 'Your Order start Cooking'), ('Your Order has been Dispatch', 'Your Order has been Dispatch'), ('Your Order has been Delivered', 'Your Order has been Delivered')], default='Accepted', max_length=100),
        ),
    ]
