from django.urls import path
from django.views.generic.base import TemplateView
from accounts.views import *

# Create the patterns
app_name = 'accounts'
urlpatterns = [
    path('signup/',UserRegistrationView.as_view(), name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path("password_change/", PasswordChangeView.as_view(), name="password_change"),
    path("password_reset/",PasswordResetView.as_view(), name="password_reset"),
    path("password_reset_done/",PasswordResetDoneView.as_view(),name='password_reset_done'),
    path("reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(), name="password_reset_complete")
    # path("reset/done/",)
    
    # path("login/", views.LoginView.as_view(), name="login"),
    # path("logout/", views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/done/",
    #     views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]
