# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from main.models import About
from main.models import Announcement
from main.models import Event
from main.models import BackgroundImage
from main.models import SplashImage
from main.models import Blog

def index(request):
    #we need all imported things as variables
    #first, the images:
    backgroundimage = BackgroundImage.objects.all().last()
    splashimage = SplashImage.objects.all().last()
    #next, the texts
    about = About.objects.all().last()
    announcements = Announcement.objects.all()
    events = Event.objects.all()
    blog = Blog.objects.all()
    #render the page
    return render(request, 'main/index.html',{
        'backgroundimage': backgroundimage,
        'splashimage': splashimage,
        'about': about,
        'announcements': announcements,
        'events': events,
        'blog': blog,
        })
    
