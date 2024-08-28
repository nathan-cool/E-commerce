from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from store.models import Customer  # Make sure to import your Customer model


@login_required
def checkout(request):
    user = request.user
    try:
        customer = Customer.objects.get(email=user.email)
    except Customer.DoesNotExist:
        customer = Customer.objects.create(
            user=user,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name
        )

    context = {
        'customer': customer
    }
    return render(request, 'checkout.html', context)
