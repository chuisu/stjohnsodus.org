# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-07 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180505_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About Section', 'verbose_name_plural': 'About Section'},
        ),
        migrations.AlterModelOptions(
            name='backgroundimage',
            options={'verbose_name': 'Background Image', 'verbose_name_plural': 'Background Image'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blog Entries'},
        ),
        migrations.AlterModelOptions(
            name='emaillistsignup',
            options={'verbose_name': 'Email List Signup', 'verbose_name_plural': 'Emails from List Signup'},
        ),
        migrations.AlterModelOptions(
            name='splashimage',
            options={'verbose_name': 'Splash Image', 'verbose_name_plural': 'Splash Image'},
        ),
        migrations.AlterField(
            model_name='about',
            name='body',
            field=models.TextField(help_text="This is the About Section that appears on the front page. This can be edited to reflect the church's mission, information about the church, and service times."),
        ),
        migrations.AlterField(
            model_name='backgroundimage',
            name='image',
            field=models.ImageField(help_text='The background image appears behind all content in the webpage. The webpage will display the most recently uploaded background image, if any. The image will automatically appear more washed-out in order to make text readable on the webpage.', upload_to='static/media'),
        ),
        migrations.AlterField(
            model_name='splashimage',
            name='image',
            field=models.ImageField(help_text='The splash image appears at the top of the front page behind the main heading. The webpage will display the most recently uploaded splash image, if any.', upload_to='static/media'),
        ),
    ]