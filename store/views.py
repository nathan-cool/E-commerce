from django.shortcuts import render
from decimal import Decimal, InvalidOperation
import re
import bleach
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.views import View
from store.models import Product, Category, Profile


class ProfileView(LoginRequiredMixin, View):
    """View to handle user profile display and updates."""
    profile_template = 'profile.html'

    def get(self, request):
        """Handle GET requests to display the user profile."""
        profile, created = Profile.objects.get_or_create(user=request.user)
        return render(
            request,
            self.profile_template,
            {'user': request.user, 'profile': profile}
        )

    def post(self, request):
        """Handle POST requests to update the user profile."""
        profile, created = Profile.objects.get_or_create(user=request.user)
        user = request.user
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        addressline1 = request.POST.get('address_line1')
        addressline2 = request.POST.get('address_line2')
        city = request.POST.get('city')
        county = request.POST.get('county')
        country = request.POST.get('country')
        eircode = request.POST.get('eircode')
        context = {"fieldValues": request.POST, "profile": profile}

        # Validate and update email
        if email and email != user.email:
            if User.objects.filter(email=email).exclude(id=user.id).exists():
                messages.error(request, 'This email is already in use.')
                return render(request, self.profile_template, context)

            if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                messages.error(request, "Invalid email format")
                return render(request, self.profile_template, context)

            user.email = email

        # Validate and update first name
        if 'first_name' in request.POST:
            first_name = request.POST['first_name']
        if not first_name:
            user.first_name = ''
        elif not re.match(r"^[A-Za-z\s]+$", first_name):
            messages.error(request, "Invalid name format")
            return render(request, self.profile_template, context)
        else:
            user.first_name = first_name

        # Validate and update password
        if password:
            if len(password) < 6:
                messages.error(
                    request,
                    "Password must be at least 6 characters long"
                )
                return render(request, self.profile_template, context)

            user.set_password(password)

        # Validate and update address line 1
        if addressline1:
            if len(addressline1) > 100:
                messages.error(
                    request,
                    "Address Line 1 must be less than 100 characters"
                )
                return render(request, self.profile_template, context)
            profile.billing_address_line1 = addressline1

        # Validate and update address line 2
        if addressline2:
            if len(addressline2) > 100:
                messages.error(
                    request,
                    "Address Line 2 must be less than 100 characters"
                )
                return render(request, self.profile_template, context)
            profile.billing_address_line2 = addressline2

        # Validate and update city
        if city:
            if len(city) > 100:
                messages.error(
                    request,
                    "City must be less than 500 characters"
                )
                return render(request, self.profile_template, context)
            profile.city = city

        # Validate and update county
        if county:
            if len(county) > 100:
                messages.error(
                    request,
                    "County must be less than 100 characters"
                )
                return render(request, self.profile_template, context)
            profile.county = county

        # Validate and update eircode
        if eircode:
            if len(eircode) > 12:
                messages.error(
                    request,
                    "Eircode must be less than 12 characters"
                )
                return render(request, self.profile_template, context)
            profile.eircode = eircode

        # Validate and update country
        if country:
            if len(country) > 100:
                messages.error(
                    request,
                    "Country must be less than 100 characters"
                )
                return render(request, self.profile_template, context)
            profile.country = country

        user.save()
        profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')


def home(request):
    """Render the home page with all products."""
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    """Render the about page."""
    return render(request, 'about.html')


def product(request, pk):
    """Render the product detail page."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})


def category(request, foo):
    """Render the category page with products belonging to the category."""
    try:
        category = get_object_or_404(Category, name=foo)
        products = Product.objects.filter(category=category)
        if not products.exists():
            pass  # No products found in this category

        categories = Category.objects.all()
        if not categories.exists():
            raise ValueError("No categories found in the database")

        context = {
            'products': products,
            'category': category,
            'categories': categories
        }
        return render(request, 'category.html', context)

    except Category.DoesNotExist:
        return HttpResponseBadRequest(f"Category '{foo}' does not exist")
    except ValueError as e:
        return HttpResponseBadRequest(str(e))
    except Exception as e:
        return HttpResponseBadRequest(
            f"An unexpected error occurred: {str(e)}"
        )


@staff_member_required
def admin_create_product(request):
    """Allow staff members to create a new product."""
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title': 'Create Product'
    }

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            qty = request.POST.get("qty")
            price = request.POST.get('price')
            category_id = request.POST.get('category')
            description = request.POST.get('description')
            product_title_description = request.POST.get(
                'product_title_description'
            )
            custom_badge = request.POST.get('custom_badge')
            image = request.FILES.get('image')

            # Validate required fields
            if not all([name, qty, price, category_id, description]):
                raise ValueError("All fields are required")

            # Convert and validate quantity
            try:
                qty = int(qty)
                if qty < 0:
                    raise ValueError
            except ValueError:
                raise ValueError("Quantity must be a non-negative integer")

            # Convert and validate price
            try:
                price = Decimal(price)
                if price <= 0:
                    raise ValueError
            except (InvalidOperation, ValueError):
                raise ValueError("Price must be a positive number")

            # Clean description
            cleaned_desc = bleach.clean(
                description,
                strip=True,
                tags=['p', 'b', 'i', 'em', 'strong', 'a', 'ul', 'ol', 'li'],
                attributes={'a': ['href']}
            )

            # Get category
            category = get_object_or_404(Category, id=int(category_id))

            # Create and save product
            product = Product(
                name=name,
                price=price,
                category=category,
                image=image,
                description=cleaned_desc,
                product_title_description=product_title_description,
                custom_badge=custom_badge,
                qty=qty
            )
            product.save()

            messages.success(request, 'Product created successfully')
            return render(request, 'create-product.html', context)

        except ValueError as e:
            messages.error(request, str(e))
        except Category.DoesNotExist:
            messages.error(request, "Selected category does not exist")
        except Exception as e:
            messages.error(
                request,
                f"An unexpected error occurred: {str(e)}"
            )

    return render(request, 'create-product.html', context)


@staff_member_required
def delete_product(request, pk):
    """
    Delete a product from the database.
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
                f"An error occurred while deleting the product: {str(e)}"
            )
        return redirect("home")


@staff_member_required
def edit_product(request, pk):
    """Allow users to edit a product."""
    if request.method == "POST":
        product = Product.objects.get(pk=pk)
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")

        # Validate and update quantity
        qty = int(request.POST.get("qty", 0))
        if qty < 100:
            product.qty = qty
        elif product.qty is None:
            product.qty = 0
        else:
            messages.error(
                request,
                "Quantity must be less than 100, this has defaulted to 1"
            )
            product.qty = 1

        product.description = request.POST.get("description")
        product.product_title_description = request.POST.get(
            "product_title_description"
        )
        product.custom_badge = request.POST.get("custom_badge")

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.save()
        messages.success(request, "Product updated successfully")

    product = Product.objects.get(pk=pk)
    categories = Category.objects.all()
    context = {
        "product": product,
        "categories": categories,
    }
    return render(request, "edit-product.html", context)


@staff_member_required
def admin_create_category(request):
    """Allow staff members to create a new category."""
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        category = Category(name=name)
        category.save()
        messages.success(request, 'Category created successfully')
        return redirect('admin_create_category')

    return render(request, 'create-category.html', {'categories': categories})


@staff_member_required
def delete_category(request, pk):
    """Delete a category from the database."""
    if request.method == "GET":
        category = Category.objects.get(pk=pk)
        if Product.objects.filter(category=category).exists():
            messages.error(
                request,
                "Cannot delete category with products associated with it "
                "please delete the products first"
            )
            return redirect("admin_create_category")
        category.delete()
        messages.success(request, "Category deleted successfully")
    return redirect("admin_create_category")


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
