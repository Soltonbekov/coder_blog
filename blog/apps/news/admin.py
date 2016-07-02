# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.news.models import News, Categories

admin.site.register(News)
admin.site.register(Categories)
