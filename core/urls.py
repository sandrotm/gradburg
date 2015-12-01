from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.nadzaladevi, name='nadzaladevi'),
    #url(r'^nadzaladevi/$', views.nadzaladevi, name='nadzaladevi'),
    url(r'^aboutUs/$', views.aboutUs, name='aboutUs'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^process/$', views.process, name='process'),
    url(r'^flats/$', views.flats, name='flats'),
]