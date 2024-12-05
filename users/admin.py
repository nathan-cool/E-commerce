from django.contrib import admin
from .models import Customer, Profile

# Register the Customer model


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('id', 'name', 'email', 'phone')
           # Add a filter for email

# Register the Profile model


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'county', 'eircode',
                    'country')  # Customize the list view

