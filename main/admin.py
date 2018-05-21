# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import About, Event, Announcement, Blog, SplashImage, BackgroundImage, EmailListSignup, Contact

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title' ]
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'body']
class BlogAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'body']
class SplashImageAdmin(admin.ModelAdmin):
    list_display = ['title' ]
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['title' ]
class EmailListSignupAdmin(admin.ModelAdmin):
    list_display = ['email']
class EventAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'description']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'phone', 'email']
admin.site.register(Event, EventAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SplashImage, SplashImageAdmin)
admin.site.register(BackgroundImage, BackgroundImageAdmin)
admin.site.register(EmailListSignup, EmailListSignupAdmin)
admin.site.register(Contact, ContactAdmin)
