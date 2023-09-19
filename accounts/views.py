from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy

#Local Imports
from accounts.forms import CustomUserForm

User = get_user_model()

# Create your views here.
class UserRegistrationView(CreateView):
    model = User
    form_class = CustomUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')


class MyStaticView(View):
    def get(self, request):
        static_data = 'Welcome to the home'
        
        return HttpResponse(static_data)
