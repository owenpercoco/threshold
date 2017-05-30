from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', views.profile_new, name='profile_new'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profile/(?P<slug>[-\w]+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profile/$', views.profile_detail, name='profile_detail'),
    url(r'^update/$', views.update_profile, name='update_profile'),
    url(r'^avatar/update$', views.update_avatar, name='update_avatar'),
    url(r'^logout/$', auth_views.logout,  {'next_page': '/'}),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^group/(?P<pk>\d+)/$', views.group_detail, name='group_detail'),
    url(r'^group/(?P<slug>[-\w]+)/$', views.group_detail, name='group_detail'),
    url(r'^update/group/', views.new_group, name='new_group'),
]