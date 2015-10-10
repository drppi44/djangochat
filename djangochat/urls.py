from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$', 'apps.main.views.home_view', name='home'),

    # auth
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^registration/$', 'apps.main.views.registration',
        name='registration'),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
