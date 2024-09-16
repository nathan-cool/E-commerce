from django.urls import path
from . import views as app_views
from checkout import views as checkout_views

urlpatterns = [
    path('', app_views.checkout, name='checkout'),
    path('success/', app_views.payment_success, name='payment_success'),
    path('cancelled/', app_views.payment_cancelled, name='payment_cancelled'),
    path('stripe-webhook/', checkout_views.stripe_webhook, name='stripe_webhook'),
]
