from django.conf.urls import url

from . import views

app_name = 'myadmin'

urlpatterns = [
    #url(r'^activity/$', views.activity, name='activity'),
#    url(r'^/change_aboutus/', views.change_team, name='change_team')
    url(r'^/$', views.news, name='news'),
    url(r'^/filters/activ$', views.activ, name='activ'),
    url(r'^/filters/monitor$', views.monitor, name='monitor'),
    url(r'^/filters/slider$', views.slider, name='slider'),
    url(r'^/partners/$', views.partners, name='partners'),
    url(r'^/news/$', views.news, name='news'),
    url(r'^/news_add/$', views.news_add, name='news_add'),
    url(r'^/news_update/(?P<id>[0-9]+)$', views.news_update, name='news_update'),
    url(r'^/news_delete/(?P<id>[0-9]+)$', views.news_delete, name='news_delete'),
    url(r'^/news_update_save/(?P<id>[0-9]+)$', views.news_update_save, name='news_update_save'),
    url(r'^/reference/$', views.reference, name='reference'),
    url(r'^/reference_add/$', views.reference_add, name='reference_add'),
    url(r'^/reference_add_save/$', views.reference_add_save, name='reference_add_save'),
    url(r'^/reference_update/(?P<id>[0-9]+)$', views.reference_update, name='reference_update'),
    url(r'^/reference_update_save/(?P<id>[0-9]+)$', views.reference_update_save, name='reference_update_save'),
    url(r'^/reference_delete/(?P<id>[0-9]+)$', views.reference_delete, name='reference_delete'),
    url(r'^/team/$', views.team, name='team'),
    url(r'^/team/add/$', views.team_add, name='team_add'),
    url(r'^/team/team_change/(?P<id>[0-9]+)$', views.team_change, name='team_change'),
    url(r'^/team/team_delete/(?P<id>[0-9]+)$', views.team_delete, name='team_delete'),
    url(r'^/change_aboutus/', views.change_aboutus, name='change_aboutus'),
    url(r'^/about/$', views.about, name='about')
]
