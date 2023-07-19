from articles.models import Category, Page, Post
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PageSitemap(Sitemap):
    def items(self):
        return Page.objects.filter(is_published=True)

    def location(self, obj):
        return obj.get_absolute_url()


class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(is_published=True)

    def location(self, obj):
        return obj.get_absolute_url()


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()
