from store.models import Product


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
    
    
        
        