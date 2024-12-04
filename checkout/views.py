import uuid
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from store.models import Product, OrderItem
from cart.cart import Cart
import stripe
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from checkout.models import Payment
from store.models import Order
from users.models import Profile

# Set the Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    
    """
    Handle the checkout process for authenticated users.
    """
    cart = Cart(request)
    """
    Check if the cart is empty.
    """
    if len(cart) == 0:
        messages.error(
            request,
            "Your cart is empty. Add some products before checking out."
        )
        return redirect('cart_summary')
    """
    Ensure the user is authenticated and retrieve or create their profile.
    """
    if request.user.is_authenticated:
        profile, created = Profile.objects.get_or_create(user=request.user)
        user_id = request.user.id
    else:
        return redirect('login/')

    if request.method == 'POST':

        """
        Collect and validate billing address from POST data.
        """
        billing_address = (
            f"{request.POST.get('address_line1')}, "
            f"{request.POST.get('address_line2', '')}, "
            f"{request.POST.get('city')}, "
            f"{request.POST.get('county')}, "
            f"{request.POST.get('eircode')}, "
            f"{request.POST.get('country')}"
        )

        if not billing_address:
            messages.error(
                request,
                "Please provide all required billing information."
            )
            return redirect('checkout')

        try:

            """
            Create a new order with the provided billing address and cart total.
            """
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                address=billing_address,
                date=timezone.now(),
                status=False,
                price=cart.get_total_price()
            )

            """
            Create order items for each product in the cart.
            """
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

            """
            Update the user's profile with the billing address.
            """
            if request.user.is_authenticated:
                profile.billing_address_line1 = request.POST.get(
                    'address_line1')
                profile.billing_address_line2 = request.POST.get(
                    'address_line2', '')
                profile.city = request.POST.get('city')
                profile.county = request.POST.get('county')
                profile.eircode = request.POST.get('eircode')
                profile.country = request.POST.get('country')

                profile.save()

            """
            Prepare line items for Stripe checkout session.
            """
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

            """
            Create a Stripe checkout session.
            """
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=(
                    request.build_absolute_uri(reverse('payment_success')) +
                    '?session_id={CHECKOUT_SESSION_ID}'
                ),
                cancel_url=request.build_absolute_uri(
                    reverse('payment_cancelled')),
                metadata={'order_id': order.id},
            )

            """
            Create a payment record with pending status.
            """
            Payment.objects.create(
                user=request.user if request.user.is_authenticated else None,
                order=order,
                profile=profile if request.user.is_authenticated else None,
                amount=cart.get_total_price(),
                stripe_payment_intent_id='',
                status='pending'
            )

            return redirect(checkout_session.url, code=303)

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('checkout')

    else:
        """
        Render the checkout page with the user's profile and cart details.
        """
        profile = (
            Profile.objects.get(user=request.user)
            if request.user.is_authenticated
            else Profile()
        )
        billing_address = (
            f"{profile.billing_address_line1}, "
            f"{profile.billing_address_line2}, "
            f"{profile.city}, "
            f"{profile.county}, "
            f"{profile.eircode}, "
            f"{profile.country}"
        )

        context = {
            'cart': cart,
            'profile': profile,
            'billing_address': billing_address,
            'total_price': cart.get_total_price(),
        }
        return render(request, 'checkout.html', context)


def payment_success(request):
    """
    Handle successful payment by updating order and payment records.
    """
    session_id = request.GET.get('session_id')

    if session_id:
        try:
            """
            Retrieve the Stripe session and associated order.
            """
            session = stripe.checkout.Session.retrieve(session_id)
            order_id = session.metadata.get('order_id')
            payment_intent_id = session.payment_intent

            order = Order.objects.get(id=order_id)
            payment = Payment.objects.get(order=order)
            payment.stripe_payment_intent_id = payment_intent_id
            payment.status = 'paid'
            payment.save()
            order.status = True
            order.save()

            """
            Clear the user's cart after successful payment.
            """
            try:
                cart = Cart(request)
                cart.clear()
            except Exception as e:
                messages.error(
                    request, "An issue occurred while clearing your cart.")

            return render(request, 'payment_success.html', {'order': order})

        except stripe.error.StripeError as e:
            messages.error(request, f"Stripe error: {str(e)}")
            return redirect('home')
        except Order.DoesNotExist:
            messages.error(request, "Order does not exist.")
            return redirect('home')
        except Payment.DoesNotExist:
            messages.error(request, "Payment does not exist.")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('home')

    
def payment_cancelled(request):
    """
    Inform the user that the payment was cancelled.
    """
    messages.info(request, "Payment was cancelled.")
    
    return render(request, 'payment_cancelled.html')


@csrf_exempt
def stripe_webhook(request):
    """
    Handle Stripe webhook events to update payment and order statuses.
    """
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        """
        Verify and construct the Stripe event.
        """
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            endpoint_secret
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session.metadata.get('order_id')
        payment_intent_id = session.payment_intent

        try:
            """
            Update the payment and order records based on the webhook event.
            """
            order = Order.objects.get(id=order_id)
            payment = Payment.objects.get(order=order)
            payment.stripe_payment_intent_id = payment_intent_id
            payment.status = 'paid'
            payment.save()
            order.status = True
            order.save()

        except Order.DoesNotExist:
            pass
        except Payment.DoesNotExist:
            pass
        except Exception as e:
            return HttpResponse(status=500)

    return HttpResponse(status=200)
