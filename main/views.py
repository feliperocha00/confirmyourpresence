from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from . import models 

# Create your views here.
def home(request):
    return render(request, "home.html")

def success(request):
    return render(request, "success.html")

def notfound(request):
    return render(request, "not_found.html")

def welcome(request):
    if request.method == "POST":
        form = models.Welcome(request.POST)
        if form.find_number(form.pk.get('Telefone')):
            return render(request, "confirm.html")
        else:
            return redirect("notfound")

    return render(request, "welcome.html")

def confirm(request):
    if request.method == "POST":
        form = models.Confirm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    

    return render(request, "confirm.html")    

# Verificação: é superusuário?
# def is_admin(user):
    # return user.is_superuser

# @login_required
# @user_passes_test(is_admin)
def confirmations(request):
    confirmations = models.Confirm.objects.all()
    return render(request, "confirmations.html", {"confirmations": confirmations})

# @login_required
# @user_passes_test(is_admin)
def guests(request):
    guests = models.Guests.objects.all()
    return render(request, "guests.html", {"guests": guests})
    