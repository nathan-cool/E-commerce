import json
from google.oauth2 import id_token
from google.auth.transport import requests
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.encoding import force_str
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
import re
import os
from django.shortcuts import render
from django.http import HttpResponse


@csrf_exempt
def social_auth(request):
    """
    Authenticate a user using Google OAuth.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    token = request.POST["credential"]
    try:
        user_data = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            os.environ["GOOGLE_OAUTH_CLIENT_ID"]
        )
    except ValueError:
        return HttpResponse(status=403)

    request.session["user_data"] = user_data

    email = user_data["email"]
    User = get_user_model()
    user, created = User.objects.get_or_create(
        username=email,
        defaults={
            "email": email,
            "first_name": user_data["given_name"]
        }
    )

    user.backend = "django.contrib.auth.backends.ModelBackend"
    login(request, user)

    if created:
        messages.success(
            request,
            f"Your account has been created, {user.first_name}!"
        )
        user.is_active = True
        user.save()
        return redirect("home")

    messages.success(request, f"Welcome, {user.first_name}!")
    user.is_active = True
    user.save()
    return redirect("home")


class RegistrationView(View):
    """Handle user registration."""

    def split_name(self, name):
        """
        Split the name into first and last name.

        Args:
            name (str): The full name to split.

        Returns:
            tuple: A tuple containing first_name and last_name.
        """
        parts = name.split(" ", 1)
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else ""
        return first_name, last_name

    def get(self, request):
        """
        Render the registration page.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The rendered registration page.
        """
        return render(request, "register.html")

    def post(self, request):
        """
        Register a user.

        Args:
            request (HttpRequest): The request object containing user data.

        Returns:
            HttpResponse: Redirect to expenses page or registration page.
        """
        name = request.POST["users-name"]
        first_name, last_name = self.split_name(name)

        password = request.POST["password"]
        email = request.POST["email"]
        context = {"fieldValues": request.POST}

        if not User.objects.filter(email=email).exists():
            if len(password) < 6:
                messages.error(request, "Invalid password")
                return render(request, "register.html", context)
            if not re.match(r"^[A-Za-z\s]+$", name):
                messages.error(request, "Invalid name")
                return render(request, "register.html", context)
            if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                messages.error(request, "Invalid email")
                return render(request, "register.html", context)

            user = User.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                username=email
            )

            user.set_password(password)
            user.is_active = True  # Set the user as active
            user.save()

            messages.success(
                request,
                f"Account created successfully. Welcome, {first_name}!"
            )

            # Log the user in immediately after registration
            login(
                request,
                user,
                backend='django.contrib.auth.backends.ModelBackend'
            )

            # Redirect to the expenses page
            return redirect("home")

        messages.error(request, "Email already exists")
        return render(request, "register.html", context)


class EmailValidationView(View):
    """Handle email validation."""

    def post(self, request):
        """
        Validate the email of a user.

        Args:
            request (HttpRequest): The request object containing the email.

        Returns:
            JsonResponse: JSON response indicating email validity.
        """
        data = json.loads(request.body)
        email = data["email"]

        if not str(email).strip():
            return JsonResponse(
                {"email_error": "Email cannot be empty"},
                status=400
            )
        if User.objects.filter(email=email).exists():
            return JsonResponse(
                {"email_error": "Sorry, this email is already in use"},
                status=409
            )

        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, email):
            return JsonResponse(
                {"email_error": "Invalid email format"},
                status=400
            )

        return JsonResponse({"email_valid": True})


class UsersNameValidationView(View):
    """Handle user name validation."""

    def post(self, request):
        """
        Validate the name of a user.

        Args:
            request (HttpRequest): The request object containing the name.

        Returns:
            JsonResponse: JSON response indicating name validity.
        """
        users_name_regex = r"^[A-Za-z\s]+$"
        data = json.loads(request.body)
        users_name = data["users_name"]

        if not str(users_name).strip():
            return JsonResponse(
                {"users_name_error": "users_name cannot be empty"},
                status=400
            )

        if not re.match(users_name_regex, users_name):
            return JsonResponse(
                {"users_name_error": "Name only letters and spaces"},
                status=400
            )

        return JsonResponse({"users_name_valid": True})


class PasswordValidationView(View):
    """Handle password validation."""

    def post(self, request):
        """
        Validate the password of a user.

        Args:
            request (HttpRequest): The request object containing the password.

        Returns:
            JsonResponse: JSON response indicating password validity.
        """
        data = json.loads(request.body)
        password = data["password"]
        password_regex = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"

        if len(str(password).strip()) < 8:
            return JsonResponse(
                {"password_error": "Password must be at least 8 characters"},
                status=400
            )
        if not re.match(password_regex, password):
            return JsonResponse(
                {
                    "password_error": "Password must have upper, lower, "
                                      "and number"
                },
                status=400,
            )
        return JsonResponse({"password_valid": True})


class LoginView(View):
    """Handle user login."""

    def get(self, request):
        """
        Render the login page.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The rendered login page.
        """
        return render(request, "login.html")

    def post(self, request):
        """
        Log in a user.

        Args:
            request (HttpRequest): The request object containing login data.

        Returns:
            HttpResponse: Redirect to expenses page or login page.
        """
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email and password:
            user = authenticate(request, username=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f"Welcome, {user.first_name}!")
                    return redirect("home")
                else:
                    messages.error(request, "Account is not activated")
            else:
                messages.error(request, "Invalid login credentials")
        else:
            messages.error(request, "Please fill in all fields")

        return render(request, "register.html")


class LogoutView(View):

    """Handle user logout."""

    def post(self, request):
        """
        Log out a user.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: Redirect to login page.
        """
        logout(request)
        return redirect('home')
