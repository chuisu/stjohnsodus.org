# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.http import HttpResponse

class About(models.Model):
    def save(self, *args, **kwargs):
        if About.objects.exists() and not self.pk:
            raise ValidationError('There can only be one About section, go back and edit the existing About object')
        return super(About, self).save(*arggs, **kwargs)
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
