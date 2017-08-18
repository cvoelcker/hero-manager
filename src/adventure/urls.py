from django.conf.urls import url

from . import views

app_name = 'adventure'

urlpatterns = [
    url(r'^(?P<hero>[\w 0-9\.]+)/(?P<group>[\w 0-9\.]+)',
        views.DiaryView.as_view(),
        name='character_diary'),
    url(r'^', views.diaries_list, name='diaries'),
]


