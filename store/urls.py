from django.urls import path
from .views import *

# Define your url routes here
app_name = "store"
urlpatterns = [
    # Homepage of the DjCommerce site
    path('',StoreHome.as_view(), name='home'),
    
    # The product detail Page
    path('product/<slug:product_slug>',ProductDetailView.as_view(), name='product_detail'),
    
    # The Category list page
    path('search/<slug:category_slug>',CategoryListView.as_view(), name='category_list')
]
