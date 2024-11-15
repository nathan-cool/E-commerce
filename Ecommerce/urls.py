
from django.contrib import admin
from django.urls import path, include 
from . import settings
from django.conf.urls.static import static
from checkout.views import stripe_webhook  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('', include('authentication.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('stripe-webhook/', stripe_webhook, name='stripe_webhook'),
]


handler404 = 'store.views.custom_404_view'

