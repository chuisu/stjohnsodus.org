# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import About
from .models import Event
from .models import Announcement
from .models import Blog
from .models import SplashImage
from .models import BackgroundImage

admin.site.register(About)
admin.site.register(Event)
admin.site.register(Announcement)
admin.site.register(Blog)
admin.site.register(SplashImage)
admin.site.register(BackgroundImage)


