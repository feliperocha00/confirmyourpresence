from django.shortcuts import render, HttpResponse, redirect
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
        if form.is_valid():
            # form.save()
            return redirect("confirm")
    # else:
    #     form = ConfirmacaoPresencaForm()

    return render(request, "welcome.html")

def confirm(request):
    if request.method == "POST":
        form = models.Confirm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    

    return render(request, "confirm.html")
    

def confirmations(request):
    confirmations = models.Confirm.objects.all()
    return render(request, "confirmations.html", {"confirmations": confirmations})
    