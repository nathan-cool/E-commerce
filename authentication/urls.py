from django.urls import include, path
from .views import (
    RegistrationView,
    EmailValidationView,
    UsersNameValidationView,
    PasswordValidationView,
    LoginView,
    LogoutView,
)
from django.views.decorators.csrf import csrf_exempt
from authentication import views

urlpatterns = [
  path("login/", LoginView.as_view(), name="login"),
  path("register/", RegistrationView.as_view(), name="register"),
]
