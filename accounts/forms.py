from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.utils.translation import gettext_lazy as _


User = get_user_model()

class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class":"form-control"}),
    )
    password2 =forms.CharField(
        label=_("Password Confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class":"form-control"}),
        
    )
    class Meta:
        model = User
        fields = ['username','email','phone_number','address','profile_image','password1','password2']
        
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control",}),
            "phone_number":forms.TextInput(attrs={"class":"form-control","placeholder":"Phone Number"}),
            "address":forms.TextInput(attrs={"class":"form-control","rows":2}),
            "profile_image":forms.ClearableFileInput(attrs={"class":"form-control","accept":"image/*"}),
            # "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            # "password2":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Re-type Password"})  
            }
        help_texts = {
            "username":None,
            "password1":None,
            "password2":None,
            }


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
    # Override error_css_class to include Bootstrap's 'is-invalid' class
    class Meta:
        model = User
        fields = ["username","password"]


class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your email"}))
    class Meta:
        model = User


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter new password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
    class Meta:
        model = User
