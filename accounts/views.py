from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

#Local Imports
from accounts.forms import CustomUserForm, CustomLoginForm,CustomPasswordChangeForm, CustomPasswordResetForm, CustomSetPasswordForm

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


class LoginView(auth_views.LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'
    

class LogoutView(auth_views.LogoutView):
    template_name = 'registration/logout.html'


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'registration/password_change.html'
    form_class = CustomPasswordChangeForm
    
    
class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'

class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    # success_url = reverse_lazy('home')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password-reset-confirm.html'
    form_class = CustomSetPasswordForm


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'registration/password-reset-complete.html'
    

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password-reset-done.html'

    
