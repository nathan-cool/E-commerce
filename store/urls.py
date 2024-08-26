from django import views
from django.urls import path 
from .views import home
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('about/', views.about, name='about'),\
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>/', views.category, name='category'),
    path('create-product/', views.admin_create_product, name='admin_create_product'),
    path('delete-product/<int:pk>', views.delete_product, name='delete_product'),
    path('edit-product/<int:pk>', views.edit_product, name='edit_product'),
    path('create-category/', views.admin_create_category, name='admin_create_category'),
]
