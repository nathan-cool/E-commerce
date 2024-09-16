# checkout/urls.py

from django.urls import path
from . import views as checkout_views  
from checkout.views import stripe_webhook  

urlpatterns = [
    path('', checkout_views.checkout, name='checkout'),
    path('success/', checkout_views.payment_success, name='payment_success'),
    path('cancelled/', checkout_views.payment_cancelled, name='payment_cancelled'),
    
]
