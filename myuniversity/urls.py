from django.conf.urls import patterns, include, url
from django.contrib import admin
from register.views import *


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
