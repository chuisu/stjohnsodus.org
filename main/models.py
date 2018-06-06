# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.http import HttpResponse

class About(models.Model):
    title = 'About'
    # def save(self, *args, **kwargs):
    #    if About.objects.exists() and not self.pk:
    #        raise ValidationError('There can only be one About section, go back and edit the existing About object')
    #    return super(About, self).save(*arggs, **kwargs)
    body = models.TextField(help_text = "This is the About Section that appears on the front page. This can be edited to reflect the church's mission, information about the church, and service times.")
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

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
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog Entries"

class SplashImage(models.Model):
    title = 'Splash Image'
    image = models.ImageField(upload_to='static/media',
    help_text = "The splash image appears at the top of the front page behind the main heading. The webpage will display the most recently uploaded splash image, if any.")
#    def save(self, *args, **kwargs):
#        if About.objects.exists() and not self.pk:
#            raise ValidationError('There can only be one splash image, go back and edit the existing splash image object')
#        return super(About, self).save(*arggs, **kwargs)
    class Meta:
        verbose_name = "Splash Image"
        verbose_name_plural = "Splash Image"

class BackgroundImage(models.Model):
    title = 'Background Image'
    image = models.ImageField(upload_to='static/media',
    help_text = "The background image appears behind all content in the webpage. The webpage will display the most recently uploaded background image, if any. The image will automatically appear more washed-out in order to make text readable on the webpage.")
#    def save(self, *args, **kwargs):
#        if About.objects.exists() and not self.pk:
#            raise ValidationError('There can only be one background image, go back and edit the existing background image object')
#        return super(About, self).save(*arggs, **kwargs)
    class Meta:
        verbose_name = "Background Image"
        verbose_name_plural = "Background Image"

class Contact(models.Model):
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=256)

class EmailListSignup(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256, blank=True)
    class Meta:
        verbose_name = "Email List Signup"
        verbose_name_plural = "Emails from List Signup"
