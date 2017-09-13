from django.conf.urls import url

from . import views

app_name = 'adventure'

urlpatterns = [
    url(
        r'^(?P<group>[\w 0-9]+)/(?P<hero>[\w 0-9]+)/all_adventures$',
        views.DiaryView.as_view(),
        name='hero_diary'
    ),

    url(
        r'^(?P<group>[\w 0-9\.]+)/(?P<adventure>[\w 0-9\.]+)/all_diaries$',
        views.AdventureView.as_view(),
        name='adventure_overview'
    ),
    url(
        r'(?P<hero>[\w 0-9\.]+)/(?P<adventure>[\w 0-9\.]+)/add_entry$',
        views.AddDiaryEntryView.as_view(),
        name='add_diary_entry'
    ),
    url(
        r'(?P<hero>[\w 0-9\.]+)/(?P<adventure>[\w 0-9\.]+)$',
        views.DiaryView.as_view(),
        name='hero_adventure_diary'
    ),
]
