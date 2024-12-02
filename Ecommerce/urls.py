from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap


from Ecommerce.sitemaps import sitemaps
from checkout.views import stripe_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('', include('authentication.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('stripe-webhook/', stripe_webhook, name='stripe_webhook'),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        )
    ),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

handler404 = 'store.views.custom_404_view'
