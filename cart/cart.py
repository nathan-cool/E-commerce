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
            self.cart[product_id] = {'quantity': int(
                quantity), 'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session.modified = True

    def __len__(self):
        return sum(item.get('quantity', 0) for item in self.cart.values())

    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())
    
    def update(self, product_id, quantity):
        product_id = str(product_id)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True
        thing = self.cart
        return thing
