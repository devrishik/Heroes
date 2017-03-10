# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.index,
        name='home'
    ),
    url(
        regex=r'^merge/$',
        view=views.merge,
        name='merge'
    ),
    url(
        regex=r'^merge/(?P<hero1>[\w ]+)/(?P<hero2>[\w ]+)/$',
        view=views.merge_heroes,
        name='merge_heroes'
    ),
    url(
        regex=r'^create/$',
        view=views.create,
        name='create'
    ),
]
