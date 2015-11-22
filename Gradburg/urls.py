"""Gradburg URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^', include('core.urls', namespace='core')),               
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
