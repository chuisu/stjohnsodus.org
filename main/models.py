# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class About(models.Model):
    body = models.TextField()

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()

class SplashImage(models.Model):
    image = models.ImageField(upload_to='static/')

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='static/')
