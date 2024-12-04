from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    # Payment status options
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Linked to User
    order = models.ForeignKey(
        'store.Order', on_delete=models.SET_NULL, null=True)  # Linked to Order from store app
    profile = models.ForeignKey(
        'users.Profile', on_delete=models.SET_NULL, null=True)  # Linked to Profile from users app
    amount = models.DecimalField(
        max_digits=10, decimal_places=2)  # Payment amount
    stripe_payment_intent_id = models.CharField(
        max_length=255)  # Stripe Payment Intent ID
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')  # Payment status


    def __str__(self):
        return f"Payment of {self.amount} for {self.user.username}"
