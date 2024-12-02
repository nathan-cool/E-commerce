from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from Ecommerce.sitemaps import sitemaps
from checkout.views import stripe_webhook

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    
    # Include URLs from the store app
    path('', include('store.urls')),
    
    # Include URLs from the authentication app
    path('', include('authentication.urls')),
    
    # Include URLs from the cart app
    path('cart/', include('cart.urls')),
    
    # Include URLs from the checkout app
    path('checkout/', include('checkout.urls')),
    
    # Stripe webhook URL
    path('stripe-webhook/', stripe_webhook, name='stripe_webhook'),
    
    # Robots.txt URL
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        )
    ),
    
    # Sitemap URL
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

# Custom 404 error handler
handler404 = 'store.views.custom_404_view'
