import re
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Category
from django.contrib.admin.views.decorators import staff_member_required
import bleach
from django.views import View

# Create your views here.


class ProfileView(LoginRequiredMixin, View):
    profile_template = 'profile.html'

    def get(self, request):
        return render(request, self.profile_template, {'user': request.user})

    def post(self, request):
        user = request.user
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        context = {"fieldValues": request.POST}

        if email and email != user.email:
            if User.objects.filter(email=email).exclude(id=user.id).exists():
                messages.error(request, 'This email is already in use.')
                return render(request, self.profile_template, context)

            if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                messages.error(request, "Invalid email format")
                return render(request, self.profile_template, context)

            user.email = email

        if 'first_name' in request.POST:
            first_name = request.POST['first_name']
        if not first_name:
            user.first_name = ''
        elif not re.match(r"^[A-Za-z\s]+$", first_name):
            messages.error(request, "Invalid name format")
            return render(request, self.profile_template, context)
        else:
            user.first_name = first_name

        if password:
            if len(password) < 6:
                messages.error(
                    request, "Password must be at least 6 characters long")
                return render(request, self.profile_template, context)

            user.set_password(password)

        user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')


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
        product_title_description = request.POST.get(
            'product_title_description')
        image = request.FILES.get('image')

        category = Category.objects.get(id=int(category_id))

        custom_badge = request.POST.get('custom_badge')
        product = Product(name=name, price=price, category=category, image=image,

                          description=cleaned_desc, product_title_description=product_title_description, custom_badge=custom_badge)

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


def edit_product(request, pk):
    if request.method == "POST":
        product = Product.objects.get(pk=pk)
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.category = Category.objects.get(
            pk=request.POST.get("category"))
        product.description = request.POST.get("description")
        product.product_title_description = request.POST.get(
            "product_title_description")
        product.custom_badge = request.POST.get("custom_badge")
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        else:
            product.image = product.image
        product.save()
        messages.success(request, "Product updated successfully")
        return redirect("home")

    product = Product.objects.get(pk=pk)
    categories = Category.objects.all()
    context = {
        "product": product,
        "categories": categories,
    }
    return render(request, "edit-product.html", context)


def admin_create_category(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        category = Category(name=name)
        category.save()
        messages.success(request, 'Category created successfully')
        return redirect('admin_create_category')

    return render(request, 'create-category.html', {'categories': categories})


def delete_category(request, pk):
    if request.method == "GET":
        category = Category.objects.get(pk=pk)
        if Product.objects.filter(category=category).exists():
            messages.error(
                request,
                "Cannot delete category with products associated with it please delete the products first",
            )
            return redirect("admin_create_category")
        category.delete()
        messages.success(request, "Category deleted successfully")
    return redirect("admin_create_category")
