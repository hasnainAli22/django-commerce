from django.urls import path
from django.views.generic.base import TemplateView
from accounts.views import UserRegistrationView, MyStaticView

# Create the patterns
urlpatterns = [
    path('',TemplateView.as_view(template_name='core/index.html'),name='home'),
    path('signup/',UserRegistrationView.as_view(), name='signup'),
    path('login/',TemplateView.as_view(template_name='core/index.html'),name='login'),
    path('logout/',TemplateView.as_view(template_name='core/index.html'),name='logout')
]
