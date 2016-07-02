# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    title = models.CharField(u"Заголовок", max_length=255)
    slug = models.CharField(u"Ссылка",max_length=45, blank=True, null=True)

    class Meta:
        verbose_name = u"категория"
        verbose_name_plural = u"категории"

    def __unicode__(self):
        return "%s - %s" % (self.title, self.slug)


class News(models.Model):
    title = models.CharField(u"Заголовок", max_length=255)
    category = models.ForeignKey(Categories, blank=True, null=True) # Внешний ключ
    author = models.ForeignKey(User, blank=True, null=True)
    text = models.TextField(u"Текст")
    #media = models.ImageField(upload_to=STATIC_URL)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"новость"
        verbose_name_plural = u"новости"

    def __unicode__(self):
        return u"%s" % (self.title)
