# Generated by Django 3.0.4 on 2020-04-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200414_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='restaurantUser',
            field=models.BooleanField(default=True),
        ),
    ]
