from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    billing_address_line1 = models.CharField(max_length=100)
    billing_address_line2 = models.CharField(
        max_length=100, blank=True, null=True)
    city = models.CharField(max_length=500)
    county = models.CharField(max_length=100)
    eircode = models.CharField(max_length=12)
    country = models.CharField(max_length=100, default='Ireland')

    def __str__(self):
        return self.user.username
