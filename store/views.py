from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Category
from django.contrib.admin.views.decorators import staff_member_required
import bleach

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
        description = request.POST.get('description')
        cleaned_desc = bleach.clean(description, strip=True, tags=['p', 'b', 'i', 'em', 'strong', 'a', 'ul', 'ol', 'li'],
                                   attributes={'a': ['href']})
        product_title_description = request.POST.get('product_title_description')
        image = request.FILES.get('image')
        category = Category.objects.get(id=int(category_id))
        product = Product(name=name, price=price, category=category, image=image,
                          cleaned_desc=description, product_title_description=product_title_description)

        product.save()

        messages.success(request, 'Product created successfully')


    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title': 'Create Product'
    }
    return render(request, 'create-product.html', context)


def delete_product(request, pk):
    """
    Delete a product from the database.

    Args:
        request (HttpRequest): The request object.
        pk (int): The ID of the product to delete.

    Returns:
        HttpResponseRedirect: A redirect to the home page or an error message.
    """
    if request.method == "GET":
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            messages.success(request, "Product deleted successfully")
        except Product.DoesNotExist:
            messages.error(request, "Product not found")
        except Exception as e:
            messages.error(
                request,
                f"An error occurred while deleting the product: {str(e)}",
            )
        return redirect("home")






