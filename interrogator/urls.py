from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'questionnaire.views.index', name='index'),
    url(r'^q/new$', 'questionnaire.views.questionnaire', name='index'),
    url(r'^q/(?P<id>\d+)$', 'questionnaire.views.questionnaire', name='index'),
    url(r'^quest/(?P<id>\d+)/new$', 'questionnaire.views.respond', name='index'),
    url(r'^quest/(?P<id>\d+)/(?P<rid>\d+)$', 'questionnaire.views.respond', name='index'),
    url(r'^quest/(?P<id>\d+)/store$', 'questionnaire.views.store', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
