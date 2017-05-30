from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^colors/list', views.colors_list, name='colors_list'),
    url(r'^colors/(?P<pk>\d+)/$', views.colors_detail, name='colors_detail'),
    url(r'^colors/new/$', views.colors_new, name='colors_new'),
    url(r'^colors/(?P<pk>\d+)/edit/$', views.colors_edit, name='colors_edit'),
]