# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-23 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180416_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundimage',
            name='image',
            field=models.ImageField(upload_to='static/media'),
        ),
        migrations.AlterField(
            model_name='splashimage',
            name='image',
            field=models.ImageField(upload_to='static/media'),
        ),
    ]
