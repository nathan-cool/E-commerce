from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Category

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html')


def product(request, pk): 
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})


def category(request, foo):
    try:
        category = get_object_or_404(Category, name=foo)
        products = Product.objects.filter(category=category)
        context = {
            'products': products,
            'category': category
        }
        return render(request, 'category.html', context)
    except Category.DoesNotExist:
        messages.error(request, f"Category '{foo}' not found")
        return redirect('home')
