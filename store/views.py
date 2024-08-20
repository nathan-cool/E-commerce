from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Category
from django.contrib.admin.views.decorators import staff_member_required

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

@staff_member_required
def admin_create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')
        category = Category.objects.get(id=int(category_id))
        product = Product(name=name, price=price, category=category, image=image)

        product.save()

        messages.success(request, 'Product created successfully')

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title': 'Create Product'
    }
    return render(request, 'create-product.html', context)





