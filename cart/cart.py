from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if cart is None:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'price': str(product.price), 'quantity': 1}
        else:
            if 'quantity' not in self.cart[product_id]:
                self.cart[product_id]['quantity'] = 1
            else:
                self.cart[product_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session.modified = True

    def __len__(self):
        return sum(item.get('quantity', 0) for item in self.cart.values())

    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())
