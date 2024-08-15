from django import views
from django.urls import path # type: ignore
from .views import home
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('about/', views.about, name='about'),\
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>/', views.category, name='category'),

    
]
