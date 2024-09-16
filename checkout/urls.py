from django.urls import path
from . import views
from checkout import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),
    

]
