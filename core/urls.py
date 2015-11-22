from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^nadzaladevi/$', views.nadzaladevi, name='nadzaladevi'),
    url(r'^aboutUs/$', views.aboutUs, name='aboutUs'),
    url(r'^contact/$', views.contact, name='contact'),
]