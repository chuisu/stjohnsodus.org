from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^announcements/$', views.announcements, name='announcements'),
    url(r'^announcements/(?P<id>\d+)/', views.announcement_detail, name='announcement_detail'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^calendar/(?P<id>\d+)/', views.calendar_detail, name='calendar_detail'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<id>\d+)/', views.blog_detail, name='blog_detail'),
    url(r'^contact/', views.contact, name='contact'),
]


