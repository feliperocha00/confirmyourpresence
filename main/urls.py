from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("admin/", views.admin, name="admin"),
    path("not-found/", views.notfound, name="notfound"),
    path("already-confirmed/", views.already_confirmed, name="already_confirmed"),
    path("list-verify/", views.list_verify, name="list_verify"),
    path("confirm/", views.confirm, name="confirm_presence"),
    path("confirm/success/", views.success, name="success"),
    path("confirmations/", views.confirmations, name="confirmations"),
    path("guests/", views.guests, name="guests"),
    path("guests/add", views.import_guests, name="import_guests"),
    path("gift_list/", views.gift_list, name="gift_list"),
    path("gift_list/add/", views.add_gift, name="add_gift"),
    path("gift_list/import/", views.import_gifts, name="import_gifts"),
    path("gift/<int:gift_id>/give/", views.gift, name="gift"),
    path("gift/<int:gift_id>/edit/", views.edit_gift, name="edit_gift"),
    path("gift/<int:gift_id>/delete/", views.delete_gift, name="delete_gift"),
    path("gift/<int:gift_id>/redirect/", views.gift_redirect_warning, name="gift_redirect_warning"),
]