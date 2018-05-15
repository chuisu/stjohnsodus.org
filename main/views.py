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
from main.models import Contact
from main.forms import EmailListSignupForm

def index(request):
    #we need all imported things as variables
    #first, the images:
    backgroundimage = BackgroundImage.objects.all().last()
    splashimage = SplashImage.objects.all().last()
    #next, the texts
    about = About.objects.all().last()
    announcements = Announcement.objects.all().order_by('-date')
    events = Event.objects.all()
    blog = Blog.objects.all()
    form = EmailListSignupForm()
    if request.method == 'POST':
      form = EmailListSignupForm(request.POST)
      if form.is_valid():
        form.email = form.clean_email()
        new_email = form.save()
    #render the page
    return render(request, 'main/index.html',{
        'backgroundimage': backgroundimage,
        'splashimage': splashimage,
        'about': about,
        'announcements': announcements,
        'events': events,
        'blog': blog,
        'form': form,
        })

def announcements(request):
    backgroundimage = BackgroundImage.objects.all().last()
    splashimage = SplashImage.objects.all().last()
    announcements = Announcement.objects.all().order_by('-date')
    return render(request, 'main/announcements.html', {
        'backgroundimage': backgroundimage,
        'splashimage': splashimage,
        'announcements': announcements,
    })

def announcement_detail(request, id):
    backgroundimage = BackgroundImage.objects.all().last()
    splashimage = SplashImage.objects.all().last()
    try:
        announcement = Announcement.objects.get(id=id)
    except Announcement.DoesNotExist:
        raise Http(404) ('This announcement does not exist')
    return render(request, 'main/announcement_detail.html', {
        'announcement': announcement,
        'backgroundimage': backgroundimage,
    })

# -- LET'S MAKE A CALENDAR -- #
# check what day the month starts on
# for each day in the month, create a table cell.
# if any day of the week before 1st of month, create a blank cell
# if sunday, start new row
# if an event exists on that day, list the event
def calendar(request):
    backgroundimage = BackgroundImage.objects.all().last()
    splashimage = SplashImage.objects.all().last()
    events = Event.objects.all().order_by('-date')
    return render(request, 'main/calendar.html', {
        'backgroundimage': backgroundimage,
        'splashimage': splashimage,
        'events': events,
    })

def calendar_detail(request, id):
    backgroundimage = BackgroundImage.objects.all().last()
    splashimage = SplashImage.objects.all().last()
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        raise Http(404) ('This event does not exist')
    return render(request, 'main/calendar_detail.html', {
        'event': event,
        'backgroundimage': backgroundimage,
    })

def blog(request):
    backgroundimage = BackgroundImage.objects.all().last()
    splashimage = SplashImage.objects.all().last()
    blogentries = Blog.objects.all().order_by('-date')
    return render(request, 'main/blog.html', {
        'backgroundimage': backgroundimage,
        'splashimage': splashimage,
        'blogentries': blogentries,
    })

def blog_detail(request, id):
    backgroundimage = BackgroundImage.objects.all().last()
    splashimage = SplashImage.objects.all().last()
    try:
        blogentry = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http(404) ('This blog entry does not exist')
    return render(request, 'main/blog_detail.html', {
        'blogentry': blogentry,
        'backgroundimage': backgroundimage,
    })

def contact(request):
    backgroundimage = BackgroundImage.objects.all().last()
    splashimage = SplashImage.objects.all().last()
    contact = Contact.objects.all()
    return render(request, 'main/contact.html', {
        'backgroundimage': backgroundimage,
        'splashimage': splashimage,
        'contact': contact,
    })
    
