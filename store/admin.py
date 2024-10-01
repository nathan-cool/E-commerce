from django.contrib import admin
from .models import Product, Category, Customer, Order

# Models for backend admin
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
