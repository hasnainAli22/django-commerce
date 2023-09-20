from django.urls import path
from django.views.generic.base import TemplateView
from accounts.views import UserRegistrationView, MyStaticView,LoginView

# Create the patterns
urlpatterns = [
    path('',TemplateView.as_view(template_name='core/index.html'),name='home'),
    path('signup/',UserRegistrationView.as_view(), name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',TemplateView.as_view(template_name='core/index.html'),name='logout'),
    
    # path("login/", views.LoginView.as_view(), name="login"),
    # path("logout/", views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    # ),
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
