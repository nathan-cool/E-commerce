from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, Category  


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):

        return ['home', 'about',]

    def location(self, item):
        return reverse(item)


class StoreSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Product.objects.all()

    def location(self, item):
        return reverse('product', args=[item.pk])


class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, item):
        return reverse('category_detail', args=[item.slug])
