from django.urls import path, include
from django.contrib import admin

from . import views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', views.home, name='home'),
    path(r'api/', include('publisher.urls', namespace='publisher')),
]
