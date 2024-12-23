from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages
from django.shortcuts import render, redirect



def cart_summary(request):
    """
    View to display the cart summary.
    """
    cart = Cart(request)
    if len(cart) > 0:
        products = cart.get_products()
        quantities = cart.get_quants()
        return render(request, 'summary.html', {
            'cart': cart, 'products': products, 'quantities': quantities
        })
    else:
        return render(request, 'summary.html', {'cart': cart})


from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages
from .cart import Cart
from store.models import Product

def cart_add(request):
    """
    View to add a product to the cart.
    """
    cart = Cart(request)
    if request.method == "POST" and request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product_quantity = int(request.POST.get('quantity'))
            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product, quantity=product_quantity)
            messages.success(request, "The product was added to the cart")
            
            # Return JSON response with a redirect URL
            return JsonResponse({
                "cart_quantity": len(cart),
                "total_price": cart.get_total_price(),
                "redirect_url": "/"  # Homepage URL or any other page
            })
        
        except (ValueError, Product.DoesNotExist):
            return JsonResponse({
                "error": "An error occurred while adding the product."
            }, status=400)

    return JsonResponse({"error": "Invalid request."}, status=400)



def cart_remove(request):
    """
    View to remove a product from the cart.
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            cart.remove(product_id)
            cart_quantity = len(cart)
            response = JsonResponse({"cart_quantity": cart_quantity})
            return response
        except ValueError as e:
            return HttpResponseBadRequest(str(e))
    return HttpResponseBadRequest("Invalid request")


def cart_update(request):
    """
    View to update the quantity of a product in the cart.
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product_quantity = int(request.POST.get('quantity'))
            cart.update(product_id=product_id, quantity=product_quantity)
            cart_quantity = len(cart)
            response = JsonResponse({"cart_quantity": cart_quantity})
            return response
        except ValueError as e:
            return HttpResponseBadRequest(str(e))
    return HttpResponseBadRequest("Invalid request")


def price(request):
    """
    View to get the total price of the cart.
    """
    cart = Cart(request)
    try:
        total_price = cart.get_total_price()
        return JsonResponse({"total_price": total_price})
    except Exception as e:
        return HttpResponseBadRequest(str(e))
    


