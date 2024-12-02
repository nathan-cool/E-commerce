from django.contrib import admin
from .models import Product, Category, Customer, Order

# Registering the Product model with the admin site
admin.site.register(Product)

# Registering the Category model with the admin site
admin.site.register(Category)

# Registering the Customer model with the admin site
admin.site.register(Customer)

