from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'hero'

urlpatterns = [
    url(r'^', views.HomeView.as_view(), name='home'),
    url(r'^groups', views.groups_list, name='groups'),
    url(r'^diaries', views.diaries_list, name='diaries'),
    url(r'^profile', views.profile, name='profile')
]
