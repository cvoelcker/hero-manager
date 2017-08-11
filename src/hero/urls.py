from django.conf.urls import url

from hero import views

app_name = 'hero'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^groups/add_new', views.GroupAddView.as_view(), name='new_group'),
    url(r'^groups/add_new/success', views.GroupSuccessView.as_view(),
        name='group_add_success'),
    url(r'^groups/(?P<name>[\w ]+)', views.GroupDetailView.as_view(),
        name='group_detail'),
    url(r'^groups/(?P<name>[\w ]+)/admin', views.GroupAdminView.as_view(),
        name='group_admin'),
    url(r'^groups', views.GroupView.as_view(), name='groups'),
    url(r'^diaries', views.diaries_list, name='diaries'),
    url(r'^profile', views.profile, name='profile')
]
