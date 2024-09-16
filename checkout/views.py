from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from store.models import Product, OrderItem 
from cart.cart import Cart
from checkout.models import Order, Payment, Profile
import stripe
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


stripe.api_key = settings.STRIPE_SECRET_KEY



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

        phone = request.POST.get('phone', '').strip()


        if not billing_address:
            messages.error(
                request, "Please provide all required billing information.")
            return redirect('checkout')


        order = Order.objects.create(
            user=request.user,
            address=billing_address,
            date=timezone.now(),
            status=False,
            price=cart.get_total_price()
        )





        for item in cart:
            product = item['product']
            quantity = item['quantity']
            price = product.price * quantity

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )
        profile.billing_address_line1 = request.POST.get('address_line1')
        profile.billing_address_line2 = request.POST.get('address_line2', '')
        profile.city = request.POST.get('city')
        profile.county = request.POST.get('county')
        profile.eircode = request.POST.get('eircode')
        profile.country = request.POST.get('country')
        profile.save()

        try:
            line_items = []
            for item in cart:
                product = item['product']
                quantity = item['quantity']
                line_items.append({
                    'price_data': {
                        'currency': 'eur',
                        'unit_amount': int(product.price * 100),
                        'product_data': {
                            'name': product.name,
                        },
                    },
                    'quantity': quantity,
                })

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('payment_success')) + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(
                    reverse('payment_cancelled')),
                metadata={'order_id': order.id},
            )
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('checkout')

        payment = Payment.objects.create(
            user=request.user,
            order=order,
            profile=profile,
            amount=cart.get_total_price(),
            stripe_payment_intent_id='',
            status='pending'
        )

        return redirect(checkout_session.url, code=303)

    else:
        billing_address = (f"{profile.billing_address_line1}, "
                           f"{profile.billing_address_line2}, "
                           f"{profile.city}, "
                           f"{profile.county}, "
                           f"{profile.eircode}, "
                           f"{profile.country}")

        context = {
            'cart': cart,
            'profile': profile,
            'billing_address': billing_address,
            'total_price': cart.get_total_price(),
        }
        return render(request, 'checkout.html', context)


def payment_success(request):
    session_id = request.GET.get('session_id')

    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)
        order_id = session.metadata.get('order_id')
        payment_intent_id = session.payment_intent

        try:
            order = Order.objects.get(id=order_id)
            payment = Payment.objects.get(order=order)
            payment.stripe_payment_intent_id = payment_intent_id
            payment.status = 'paid'
            payment.save()
            order.status = True
            order.save()

            cart = Cart(request)
        except Order.DoesNotExist:
            messages.error(request, "Order does not exist.")
            return redirect('home')

    return render(request, 'payment_success.html')


def payment_cancelled(request):
    messages.info(request, "Payment was cancelled.")
    return render(request, 'payment_cancelled.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session.metadata.get('order_id')
        payment_intent_id = session.payment_intent

        try:
            order = Order.objects.get(id=order_id)
            payment = Payment.objects.get(order=order)
            payment.stripe_payment_intent_id = payment_intent_id
            payment.status = 'paid'
            payment.save()
            order.status = True
            order.save()

        except Order.DoesNotExist:
            pass

    return HttpResponse(status=200)
