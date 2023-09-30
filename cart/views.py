from django.shortcuts import render,get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.views import View
from store.models import Product
from .cart import Cart

# Create your views here.
class CartSummaryView(View):
    template_name = 'cart/cart-summary.html'
    def get(self, request):
        return render(request, self.template_name)


class CartAddView(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            product_quantity = int(request.POST.get('product_quantity'))
            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product,product_qty=product_quantity)
            
            return JsonResponse({"title":"product","id":product_id,"qty":product_quantity})

class CartDeleteView(View):
    pass

class CartUpdateView(View):
    pass
