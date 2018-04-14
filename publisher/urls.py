from django.urls import path

from . import views


app_name = 'publisher'

urlpatterns = [
    path('publish', views.PublisherView.as_view(), name='main'),
]
