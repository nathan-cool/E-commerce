from .cart import Cart

# Context processor to add the cart to the context
def cart(request):
  return {'cart': Cart(request)}

# Context processor to add the staff status to the context
def staff_status(request):
  return {'is_staff': request.user.is_staff}

from store.models import Category

# Context processor to add all categories to the context
def categories_processor(request):
  return {'categories': Category.objects.all()}