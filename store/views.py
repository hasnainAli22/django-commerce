from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Product,Category

# Create your views here.
class StoreHome(View):
    template_name = 'store/homepage.html'
    
    def get(self, request):
        products = Product.objects.all() # Retrive all project instances
        context = {'products':products}
        return render(request, self.template_name, context)
    
class ProductDetailView(View):
    template_name = 'store/product_detail.html'
    
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug )
        context = {'product':product}
        return render(request, self.template_name, context)


class CategoryListView(View):
    template_name = 'store/category_list.html'
    
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
        context = {'products':products,'category':category}
        return render(request, self.template_name, context)
        