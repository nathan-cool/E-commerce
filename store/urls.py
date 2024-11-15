from django import views
from django.urls import path
from .views import ProfileView, home
from . import views
from django.conf import settings
from django.conf.urls.static import static
# URL patterns for the app
# Includes home, about, product, and category views.
# Admin views include create, delete, and edit functionality
# Profile-related views for updating and viewing user profiles.

urlpatterns = [
    path('', home, name='home'),
    path('about/', views.about, name='about'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>/', views.category, name='category'),
    path(
        'create-product/', views.admin_create_product,
        name='admin_create_product'
    ),
    path(
        'delete-product/<int:pk>', views.delete_product,
        name='delete_product'
    ),
    path(
        'edit-product/<int:pk>', views.edit_product,
        name='edit_product'
    ),
    path(
        'create-category/', views.admin_create_category,
        name='admin_create_category'
    ),
    path(
        'delete-category/<int:pk>', views.delete_category,
        name='delete_category'
    ),
    path('update-user/', ProfileView.as_view(), name='update_user'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

