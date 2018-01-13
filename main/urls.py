"""
https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
]
