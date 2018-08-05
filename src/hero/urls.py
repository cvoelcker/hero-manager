from django.conf.urls import url

from . import views

app_name = 'hero'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^groups$', views.GroupView.as_view(), name='groups'),
    url(r'^groups/add_new$', views.GroupAddView.as_view(), name='new_group'),
    url(r'^groups/(?P<group>[\w 0-9-\']+)$', views.GroupDetailView.as_view(),
        name='group_detail'),
    url(r'^groups/(?P<group>[\w 0-9-\']+)/add_hero$',
        views.GroupAddHeroView.as_view(),
        name='group_add_hero'),
    url(r'^groups/(?P<group>[\w 0-9-\']+)/admin$',
        views.GroupAdminView.as_view(),
        name='group_admin'),
    url(r'^groups/(?P<group>[\w 0-9-\']+)/(?P<hero>[\w 0-9-\']+)$',
        views.GroupHeroView.as_view(), name='hero_overview'),
    url(
        r'^groups/(?P<group>[\w 0-9-\']+)/(?P<hero>[\w 0-9-\']+)/charsheet$',
        views.HeroCharsheetView.as_view(),
        name='character_sheet'),
    url(
        r'^groups/(?P<group>[\w 0-9-\']+)/(?P<hero>[\w 0-9-\']+)/charsheet/upload$',
        views.HeroAddCharsheetView.as_view(), name='upload_char_sheet'),
    url(r'^player/(?P<player>[\w 0-9-\']+)$', views.ProfileView.as_view(),
        name='profile'),
]

#from django.conf.urls import url

#from . import views

#app_name = 'adventure'

#urlpatterns = [
#    url(
#        r'^(?P<group>[\w 0-9-\'\.]+)/(?P<hero>[\w 0-9-\'\.]+)/all_adventures$',
#        views.DiaryView.as_view(),
#        name='hero_diary'
#    ),

#    url(
#        r'^(?P<group>[\w 0-9-\'\.]+)/(?P<adventure>[\w 0-9-\'\.]+)/all_diaries$',
#        views.AdventureView.as_view(),
#        name='adventure_overview'
#    ),
#    url(
#        r'(?P<adventure>[\w 0-9-\'\.]+)/add_entry$',
#        views.AddDiaryEntryView.as_view(),
#        name='add_diary_entry'
#    ),
#    url(
#        r'(?P<hero>[\w 0-9-\'\.]+)/(?P<adventure>[\w 0-9-\'\.]+)/(?P<id>[\w 0-9-\'\.]+)$',
#        views.DiaryEntryView.as_view(),
#        name='hero_adventure_diary_entry'
#    ),
#    url(
#        r'(?P<hero>[\w 0-9-\'\.]+)/(?P<adventure>[\w 0-9-\'\.]+)$',
#        views.DiaryView.as_view(),
#        name='hero_adventure_diary'
#    ),
#]
