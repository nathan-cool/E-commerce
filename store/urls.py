from django.urls import path # type: ignore
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
