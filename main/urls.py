from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("not-found/", views.notfound, name="notfound"),
    path("success/", views.success, name="success"),
    path("confirm/", views.confirm, name="confirm_presence"),
    path("confirmations/", views.confirmations, name="confirmations")
    # path("home", views.home, name="Home"),
]