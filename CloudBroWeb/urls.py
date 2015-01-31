from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'CloudBroWeb.views.home', name='home'),
                       url(r'^blog/', include('blog.urls', namespace='blog')),
                       url(r'^twitch/', include('twitch.urls', namespace='twitch')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
