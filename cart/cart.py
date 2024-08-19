import logging
from store.models import Product  # Add this import

logger = logging.getLogger(__name__)

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if cart is None:
            cart = self.session['session_key'] = {}
        self.cart = cart
        logger.debug(f"Cart initialized: {self.cart}")

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': int(quantity), 'price': str(product.price)}
        else:
            if isinstance(self.cart[product_id], dict):
                self.cart[product_id]['quantity'] += int(quantity)
            else:
                self.cart[product_id] = {'quantity': int(quantity), 'price': str(product.price)}
        self.save()
        logger.debug(f"Product added to cart: {product_id}, New cart: {self.cart}")

    def save(self):
        self.session.modified = True
        logger.debug("Cart saved")

    def __len__(self):
        logger.debug(f"Calculating cart length. Cart: {self.cart}")
        return sum(item['quantity'] if isinstance(item, dict) else item for item in self.cart.values())

    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        logger.debug(f"Retrieved products: {products}")
        return products
    
    def get_quants(self):
        logger.debug(f"Retrieving quantities: {self.cart}")
        return self.cart
    
    def get_total_price(self):
        total = sum(float(item['price']) * item['quantity'] if isinstance(item, dict) else 0 for item in self.cart.values())
        logger.debug(f"Calculated total price: {total}")
        return total
    
    def update(self, product_id, quantity):
        product_id = str(product_id)
        if product_id in self.cart:
            if isinstance(self.cart[product_id], dict):
                self.cart[product_id]['quantity'] = int(quantity)
            else:
                product = Product.objects.get(id=product_id)
                self.cart[product_id] = {'quantity': int(quantity), 'price': str(product.price)}
        self.save()
        logger.debug(f"Updated cart: {self.cart}")
        return self.cart