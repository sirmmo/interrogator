from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'questionnaire.views.index', name='index'),
    url(r'^q/new$', 'questionnaire.views.questionnaire', name='index'),
    url(r'^q/(?P<id>\d+)$', 'questionnaire.views.questionnaire', name='index'),
    url(r'^quest/(?P<id>\d+)/new$', 'questionnaire.views.respond', name='index'),
    url(r'^quest/(?P<id>\d+)/image$', 'questionnaire.views.header', name='index'),
    url(r'^quest/(?P<id>\d+)/(?P<rid>\d+)$', 'questionnaire.views.respond', name='index'),
    url(r'^quest/(?P<id>\d+)/store$', 'questionnaire.views.store', name='index'),
    url(r'^quest/(?P<id>\d+)/deactivate$', 'questionnaire.views.deactivate', name='index'),
    url(r'^quest/(?P<id>\d+)/activate$', 'questionnaire.views.activate', name='index'),
    url(r'^quest/(?P<id>\d+)/csv$', 'questionnaire.views.csv', name='index'),

    url(r'^response/(?P<rid>\d+)$', 'questionnaire.views.response', name='response'),
    url(r'^response/(?P<rid>\d+)/img$', 'questionnaire.views.image', name='image'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),


    url(r'^admin/', include(admin.site.urls)),
)
