from .cart import Cart
from django.contrib.auth.decorators import login_required

def cart(request):
  return {'cart': Cart(request)}


def staff_status(request):
    print('staff_status')
    return {'is_staff': request.user.is_staff}
