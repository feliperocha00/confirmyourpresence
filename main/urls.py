from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("not-found/", views.notfound, name="notfound"),
    path("already-confirmed/", views.already_confirmed, name="already_confirmed"),
    path("confirm/", views.confirm, name="confirm_presence"),
    path("confirm/success/", views.success, name="success"),
    path("confirmations/", views.confirmations, name="confirmations"),
    path("guests/", views.guests, name="guests"),
    path("guests/add", views.add_guests, name="add_guests"),
    path("gift_list/", views.gift_list, name="gift_list"),
    path("gift/<int:gift_id>/give/", views.gift, name="gift")
]