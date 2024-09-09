from .cart import Cart
from django.contrib.auth.decorators import login_required


def cart(request):
  return {'cart': Cart(request)}


def staff_status(request):
    return {'is_staff': request.user.is_staff}


from store.models import Category

def categories_processor(request):
    return {'categories': Category.objects.all()}