from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    if len(cart) > 0: 
        products = cart.get_products()
        quantities = cart.get_quants()  # Add parentheses here
        return render(request, 'summary.html', {'cart': cart, 'products': products, 'quantities': quantities})
    else:
        return render(request, 'summary.html', {'cart': cart})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_quantity)
        cart_quantity = len(cart)
        response = JsonResponse(
            {"cart_quantity": cart_quantity, 'total_price': cart.get_total_price()})
        return response

def cart_remove(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.remove(product_id)
        cart_quantity = len(cart)
        response = JsonResponse({"cart_quantity": cart_quantity})
        return response
   

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('quantity'))
        cart.update(product_id=product_id, quantity=product_quantity)
        cart_quantity = len(cart)
        response = JsonResponse({"cart_quantity": cart_quantity})
        return response
    
def price(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    return JsonResponse({"total_price": total_price})
