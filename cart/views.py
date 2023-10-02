from django.shortcuts import render,get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.views import View
from store.models import Product
from .cart import Cart

# Create your views here.
class CartSummaryView(View):
    template_name = 'cart/cart-summary.html'
    def get(self, request):
        self.cart = Cart(request)
        return render(request, self.template_name, {"cart":self.cart})


class CartAddView(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            product_quantity = int(request.POST.get('product_quantity'))
            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product,product_qty=product_quantity)
            product_qty = cart.__len__()
            
            return JsonResponse({"qty":product_qty})

class CartDeleteView(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            product_id = str(request.POST.get('product_id'))
            cart.delete(product=product_id)
            
            subtotal = cart.get_total()
            return JsonResponse({'qty':cart.__len__(), 'subtotal':subtotal })
            

class CartUpdateView(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            product_quantity = int(request.POST.get('product_quantity'))
            cart.update(product_id, product_quantity)
            
            
            product_price = cart.product_price(product_id, product_quantity)
            subtotal = cart.get_total()
            return JsonResponse({'qty':cart.__len__(), 'subtotal':subtotal,'product_price':product_price})

