# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from apps.news.models import Categories, News

class NewsTestCase(TestCase):

    def setUp(self):
        self.category = Categories.objects.create(
            title = 'TestCategory', slug='test-category'
        )
        self.news = News.objects.create(
            title = 'TestFreshNews', category = self.category
        )

        self.client = Client()

    def test_simple(self):
        self.assertEqual(1 + 1, 2)

    def test_category_title_creation(self):
        self.assertEqual(self.category.title, 'TestCategory')

    def test_category_slug_creation(self):
        self.assertEqual(self.category.slug, 'test-category')

    def test_news_title_creation(self):
        self.assertEqual(self.news.title, 'TestFreshNews')

    def test_news_category_slug(self):
        self.assertEqual(self.news.category.slug, 'test-category')

    def test_index_page(self):
        response = self.client.get('/news/')
        print dir(response)
        self.assertEqual(response.status_code, 200)

    def test_index_page_template(self):
        response = self.client.get('/news/')
        self.assertTemplateUsed(response, 'news/news_list.html')

    def test_category_page(self):
        response = self.client.get('/news/%s/' % self.category.slug)
        self.assertEqual(response.status_code, 200)

    def test_indefined_category_page(self):
        response = self.client.get('/news/undefined/')
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        pass
