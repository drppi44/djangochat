from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$', 'apps.main.views.home_view', name='home'),


    url(r'^admin/', include(admin.site.urls)),
)
