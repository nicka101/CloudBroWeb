from django.conf.urls import patterns, url
from twitch import views


urlpatterns = patterns('',
                       url(r'^live_streams$', views.available_streams, name='live_streams'),
                       )

