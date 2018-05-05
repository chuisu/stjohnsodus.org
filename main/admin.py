# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import About
from .models import Event
from .models import Announcement
from .models import Blog
from .models import SplashImage
from .models import BackgroundImage
from .models import EmailListSignup

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title' ]
class EventAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'description']
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'body']
class BlogAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'description']
class SplashImageAdmin(admin.ModelAdmin):
    list_display = ['title' ]
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['title' ]
class EmailListSignupAdmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(About)
admin.site.register(Event)
admin.site.register(Announcement)
admin.site.register(Blog)
admin.site.register(SplashImage)
admin.site.register(BackgroundImage)
admin.site.register(EmailListSignup)

