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
    path("register/", RegistrationView.as_view(), name="register"),
    path(
        "authentication/validate-email",
        csrf_exempt(EmailValidationView.as_view()),
        name="validate-email",
    ),
    path(
        "authentication/validate-name",
        csrf_exempt(UsersNameValidationView.as_view()),
        name="validate-name",
    ),
    path(
        "authentication/validate-password",
        csrf_exempt(PasswordValidationView.as_view()),
        name="validate-password",
    ),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
