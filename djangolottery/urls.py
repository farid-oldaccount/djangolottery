from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'djangolottery.apps.website.views.index'),
    url(r'^api/participate/', 'djangolottery.apps.api.views.participate'),
    url(r'^draw/', 'djangolottery.apps.website.views.draw'),
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
