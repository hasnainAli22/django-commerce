from store.models import Product
from decimal import Decimal


class Cart():
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('cart-session')
        if 'cart-session' not in self.session:
            cart = self.session['cart-session'] = {}
        self.cart = cart
    
    
    def add(self, product, product_qty):
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty
        else:
            pass
            self.cart[product_id] = {'price':float(product.price), 'qty':product_qty}
        
        self.session.modified = True
    
    
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
    
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item
    
    
    def get_total(self, decimal_places=2):
        total = sum(Decimal(item['price']) * Decimal(item['qty']) for item in self.cart.values()) 
        precision = Decimal('0.1') ** decimal_places
        return Decimal(total).quantize(precision)
    
    def product_price(self, product_id, product_quantity):
        product_id = str(product_id)
        total = Decimal(self.cart[product_id]['price']) * Decimal(product_quantity)
        precision = Decimal('0.1') ** 2
        return Decimal(total).quantize(precision)
    
    def delete(self, product):
        if product in self.cart:
            del self.cart[product]
        self.session.modified = True
    
    def update(self, product_id, product_quantity):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_quantity
        self.session.modified = True