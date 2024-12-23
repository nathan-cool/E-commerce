from django.contrib import admin
from store.models import Order, OrderItem
from checkout.models import Payment
  # Import from the correct module


class OrderItemInline(admin.TabularInline):
    model = OrderItem  # Use the OrderItem model
    extra = 0  # Do not display extra empty rows

class paymentInline(admin.TabularInline):
    model = Payment
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quantity', 'price',
                    'address', 'phone', 'date', 'status')
    search_fields = ('user__username', 'id', 'address', 'phone')
    list_filter = ('status', 'date')
    inlines = [OrderItemInline]  # Add OrderItem as inline for Order
