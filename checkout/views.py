from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from store.models import Order, Profile, Product
from cart.cart import Cart
from checkout.models import Payment


def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.error(
            request, "Your cart is empty. Add some products before checking out.")
        return redirect('cart_summary')

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':

        billing_address = (f"{request.POST.get('address_line1')}, "
                   f"{request.POST.get('address_line2', '')}, "
                   f"{request.POST.get('city')}, "
                   f"{request.POST.get('county')}, "
                   f"{request.POST.get('eircode')}, "
                   f"{request.POST.get('country')}")

        for product_id, item in cart.cart.items():
            product = Product.objects.get(id=product_id)
            order, created = Order.objects.update_or_create(
                user=request.user,
                defaults={
                    'product': product,
                    'quantity': item['quantity'],
                    'price': float(item['price']) * item['quantity'],
                    'address': billing_address,
                    'phone': request.POST.get('phone', ''),
                    'date': timezone.now(),
                    'status': False
                }
            )
            order.save()


        payment = Payment(
            user=request.user,
            order=order,
            profile=profile,
            amount=cart.get_total_price(),
            stripe_payment_intent_id='123',
            status='paid'
        )
        

        profile.billing_address_line1 = request.POST.get('address_line1')
        profile.billing_address_line2 = request.POST.get('address_line2', '')
        profile.city = request.POST.get('city')
        profile.county = request.POST.get('county')
        profile.eircode = request.POST.get('eircode')
        profile.country = request.POST.get('country')
        profile.save()

        cart.cart.clear()
        cart.save()

        messages.success(request, "Your order has been placed successfully!")
        return redirect('home')


    products = cart.get_products()
    quantities = cart.get_quants()

    context = {
        'products': products,
        'quantities': quantities,
        'cart': cart,
        'profile': profile,
        'total_price': cart.get_total_price(),
        'user': request.user
    }
    return render(request, 'checkout.html', context)
