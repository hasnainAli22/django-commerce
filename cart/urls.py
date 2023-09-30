from django.urls import path
from .models import *
from .views import *

app_name = 'cart' # Useful for getting the exact url from any app

urlpatterns = [
    path('', CartSummaryView.as_view(),name='cart-summary'),
    path('add/', CartAddView.as_view(),name='cart-add'),
    path('delete/',CartDeleteView.as_view(), name='cart-delete'),
    path('update/',CartUpdateView.as_view(), name='cart-update')
]
