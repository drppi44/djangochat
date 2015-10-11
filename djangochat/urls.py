from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$', 'apps.main.views.home_view', name='home'),

    # chat
    url(r'^ajax/chat/add/', 'apps.main.views.chat_add', name='chat-add'),
    url(r'^ajax/chat/get/', 'apps.main.views.chat_get', name='chat-get'),

    # auth
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^registration/$', 'apps.main.views.registration',
        name='registration'),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
