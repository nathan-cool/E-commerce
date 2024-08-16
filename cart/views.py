from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, 'summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        cart_quantity = len(cart)  # Use len() instead of __len__()
        response = JsonResponse({"cart_quantity": cart_quantity})
        return response


def cart_remove(request):
    return render(request, 'remove.html')


def cart_update(request):
    return render(request, 'update.html')
