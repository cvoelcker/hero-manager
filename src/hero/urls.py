from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view()),
    url(r'^groups$', views.groups_list, name='groups list')
]
