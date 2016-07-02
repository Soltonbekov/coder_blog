# -*- coding: utf-8 -*-

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from apps.news.models import News, Categories

def news_list(request):
    context = {
        'news': News.objects.all().order_by('-created_at'),
        'categories': Categories.objects.all(),
    }
    
    return render(request, 'news/news_list.html', context)


def news_by_category(request, slug):
    try:
        category = Categories.objects.get(slug=slug)
    except Categories.DoesNotExist:
        raise Http404
    context = {
        'category_news': category.news_set.all(),
        'categories': Categories.objects.all(),
    }

    return render(request, 'news/news_by_category.html', context)

def news_detail(request, news_id):
    try:
        details = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404
    context = {
        'categories': Categories.objects.all(),
        'news': details,
    }

    return render(request, 'news/news_detail.html', context)

def about(requets):
    categories = Categories.objects.all()
    return render(requets, 'news/about.html', locals())

def contacts(requets):
    context = {
        'categories': Categories.objects.all(),
    }

    return render(requets, 'news/contacts.html', context)
