from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("not-found/", views.notfound, name="notfound"),
    path("success/", views.success, name="success"),
    path("confirm/", views.confirm, name="confirm_presence"),
    path("confirmations/", views.confirmations, name="confirmations"),
    path("guests/", views.guests, name="guests"),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout')
]