from django.conf.urls import url
# from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.about, name='about'),
    url(r'^$', views.contact, name='contact'),
    url(r'^$', views.location, name='location'),
]
