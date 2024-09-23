from store.models import Product


class Cart:
    """A shopping cart class that handles cart op within a user's session."""

    def __init__(self, request):
        """Initialize the cart"""
        if not hasattr(request, 'session'):
            raise AttributeError(
                "The request object must have a 'session' attribute.")
        self.session = request.session
        cart = self.session.get('session_key')
        if cart is None:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def __iter__(self):
        """Iterate over the items in the cart and attach the Product."""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            cart_item = self.cart[str(product.id)].copy()
            cart_item['product'] = product
            yield cart_item

    def add(self, product, quantity):
        """Add a product to the cart or update its quantity."""
        if not isinstance(product, Product):
            raise ValueError("The 'product' must be an instance of Product.")
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("The quantity must be a positive integer.")
        except (ValueError, TypeError) as e:
            raise ValueError("Please enter a positive integer.") from e

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product.price)
            }
        else:
            if isinstance(self.cart[product_id], dict):
                self.cart[product_id]['quantity'] += quantity
            else:
                self.cart[product_id] = {
                    'quantity': quantity,
                    'price': str(product.price)
                }
        self.save()

    def save(self):
        """Mark the session as modified to ensure it is saved."""
        self.session.modified = True

    def __len__(self):
        """Return the total number of items in the cart."""
        return sum(
            item['quantity'] if isinstance(item, dict) else 0
            for item in self.cart.values()
        )

    def get_products(self):
        """Retrieve Product instances for the items in the cart."""
        try:
            product_ids = self.cart.keys()
            products = Product.objects.filter(id__in=product_ids)
            return products
        except Product.DoesNotExist:
            return []
        except Exception as e:
            # Log the exception if needed
            print(f"An error occurred: {e}")
            return []

    def get_quants(self):
        """Get the quantities of all items in the cart."""
        return self.cart

    def get_total_price(self):
        """Calculate the total price of all items in the cart."""
        return sum(
            float(item['price']) *
            item['quantity'] if isinstance(item, dict) else 0
            for item in self.cart.values()
        )

    def update(self, product_id, quantity):
        """Update the quantity of a product in the cart."""
        product_id = str(product_id)
        try:
            quantity = int(quantity)
            if quantity <= 0:
                self.remove(product_id)
                return self.cart
        except (ValueError, TypeError) as e:
            raise ValueError("Please enter a positive integer.") from e

        if product_id in self.cart:
            if isinstance(self.cart[product_id], dict):
                self.cart[product_id]['quantity'] = quantity
            else:
                try:
                    product = Product.objects.get(id=product_id)
                    self.cart[product_id] = {
                        'quantity': quantity,
                        'price': str(product.price)
                    }
                except Product.DoesNotExist:
                    self.remove(product_id)
        self.save()
        return self.cart

    def remove(self, product_id):
        """Remove a product from the cart."""
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        return self.cart
