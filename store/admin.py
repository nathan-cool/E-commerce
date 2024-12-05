from django.contrib import admin
from .models import Category, Product

# Register the Category model


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Customize the list view
    search_fields = ('name',)     # Add a search bar for categories


# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',
                    'is_sale', 'sale_price', 'qty', 'updated_at')
    # Add filters for sale status and category
    list_filter = ('is_sale', 'category')
    search_fields = ('name', 'description')  # Add a search bar
    readonly_fields = ('updated_at',)       
