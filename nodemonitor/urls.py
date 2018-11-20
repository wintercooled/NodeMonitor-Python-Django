from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^', include('dashboard.urls')),
]