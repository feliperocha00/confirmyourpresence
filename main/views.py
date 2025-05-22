from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from . import models
from openpyxl import Workbook

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
        guests = form.find_number(form.pk.get('Telefone'))
        if guests:
            return render(request, "confirm.html", {'guests': guests})
        else:
            return redirect("notfound")

    return render(request, "welcome.html")

def confirm(request):
    if request.method == 'POST':
        form = models.Guests(request.POST)
        total_rows = int(request.POST.get('total_rows', 0))
        items = []
        for i in range(1, total_rows + 1):
            name = request.POST.get(f'guest_name_{i}')
            confirmation = request.POST.get(f'guest_confirmation_{i}')

            guest = form.find_guest(name)
            if guest:
                form.save()
                # items.append({'name': name, 'quantity': confirmation})
        
        return render(request, 'success.html', {'items': items})

    return render(request, "confirm.html")    

# Verificação: é superusuário?
# def is_admin(user):
    # return user.is_superuser

# @login_required
# @user_passes_test(is_admin)
def confirmations(request):
    confirmations = models.Confirm.objects.all()

    if request.method == "POST":
        # form = models.Confirmations(request.POST)
        # form.export(confirmations)
        # return render(request, "success.html")
        
        # Criar o workbook e a planilha
        wb = Workbook()
        ws = wb.active
        ws.title = "Confirmações"

        # Cabeçalhos
        ws.append(["Nome", "Confirmação"])

        # Linhas com dados
        for c in confirmations:
            status = "Confirmado" if c.confirm else "Não vai"
            ws.append([c.name, status])

        # Criar resposta
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = 'attachment; filename="confirmacoes.xlsx"'

        # Salvar no response
        wb.save(response)
        return response

    return render(request, "confirmations.html", {"confirmations": confirmations})

# @login_required
# @user_passes_test(is_admin)
def guests(request):
    guest_list = models.Guests.objects.all()
    return render(request, "guests.html", {"guests": guest_list})
    
def add_guests(request):
    if request.method == "POST":
        IoBytes = request.FILES.get('file').file

        if models.Guests.import_guests(IoBytes):
            return redirect("guests")
    
    return render(request, "add_guests.html")