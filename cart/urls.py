"""
URL configuration for the cart application.

This module defines the URL patterns for the cart-related views in the 
e-commerce application.

URL patterns:
- 'summary/': Displays the cart summary.
- 'add/': Adds an item to the cart.
- 'remove/': Removes an item from the cart.
- 'update/': Updates the quantity of an item in the cart.
- 'price/': Retrieves the price details of the cart.
- 'accounts/login/': Displays the login view.

"""


from django.urls import path
from authentication.views import LoginView
from . import views

urlpatterns = [
    path('summary/', views.cart_summary, name='cart_summary'),
    path('add/', views.cart_add, name='cart_add'),
    path('remove/', views.cart_remove, name='cart_remove'),
    path('update/', views.cart_update, name='cart_update'),
    path('price/', views.price, name='cart_price'),
    path('accounts/login/', LoginView.as_view(), name='login'),

]
