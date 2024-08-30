from store.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if cart is None:
            cart = self.session['session_key'] = {}
        self.cart = cart

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

    def save(self):
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] if isinstance(item, dict) else item for item in self.cart.values())

    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
    
        return self.cart
    
    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] if isinstance(item, dict) else 0 for item in self.cart.values())
    
    def update(self, product_id, quantity):
        product_id = str(product_id)
        if product_id in self.cart:
            if isinstance(self.cart[product_id], dict):
                self.cart[product_id]['quantity'] = int(quantity)
            else:
                product = Product.objects.get(id=product_id)
                self.cart[product_id] = {'quantity': int(quantity), 'price': str(product.price)}
        self.save()
        return self.cart
    
    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        return self.cart