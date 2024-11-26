
"""
This module defines URL patterns for the Checkout application.

The `urlpatterns` list routes URLs to views. The available paths include:
- The root path ('') routed to the `checkout` view.
- The 'success/' path routed to the `payment_success` view.
- The 'cancelled/' path routed to the `payment_cancelled` view.
- The 'webhook/' path routed to the `stripe_webhook` view.
"""

from django.urls import path
from . import views as checkout_views
from checkout.views import stripe_webhook

urlpatterns = [
    path('', checkout_views.checkout, name='checkout'),
    path('payment_success', checkout_views.payment_success, name='payment_success'),
    path(
        'cancelled/',
        checkout_views.payment_cancelled,
        name='payment_cancelled',
    ),
    path('webhook/', stripe_webhook, name='stripe_webhook'),
]
