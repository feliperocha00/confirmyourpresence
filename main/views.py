from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from . import forms
from openpyxl import Workbook

@login_required
def admin(request):
    return render(request, "admin_page.html")

def success(request):
    return render(request, "success.html")

def notfound(request):
    return render(request, "not_found.html")

def already_confirmed(request):
    if request.method == "POST":
        form = models.Welcome(request.POST)
        guests = form.find_number(form.pk.get('Telefone'))
        if guests:
            if any([g.confirm for g in guests]):
                return render(request, "confirm.html", {'guests': guests})
            else:
                return render(request, "already_confirmed.html", {'guests': guests})
        else:
            return redirect("notfound")
        
    return render(request, "already_confirmed.html")

def welcome(request):
    return render(request, "welcome.html")

def list_verify(request):
    if request.method == "POST":
        model = models.ListVerify(request.POST)
        guests = model.find_number(model.pk.get('Telefone'))
        if guests:
            if any([g.confirm for g in guests]):
                return render(request, "confirm.html", {'guests': guests})
            else:
                return render(request, "already_confirmed.html", {'guests': guests})
        else:
            return redirect("notfound")

    return render(request, "list_verify.html")

def confirm(request):
    if request.method == 'POST':
        total_rows = int(request.POST.get('total_rows', 0))

        for i in range(1, total_rows + 1):
            guest_name = request.POST.get(f'guest_name_{i}')
            guest_confirmation = request.POST.get(f'guest_confirmation_{i}')
            
            if guest_name:
                is_confirmed = guest_confirmation is not None

                try:
                    guest = models.Guests.objects.get(name=guest_name)
                    guest.confirm = is_confirmed
                    guest.save()
                except models.Guests.DoesNotExist:
                    raise UserWarning("Convidado não encontrado. Comunique o Noivo!")
                
        return redirect('success')
    return render(request, "confirm.html")    

@login_required
def confirmations(request):
    guests = models.Guests.objects.all()

    if request.method == "POST":        
        # Criar o workbook e a planilha
        wb = Workbook()
        ws = wb.active
        ws.title = "Confirmações"

        # Cabeçalhos
        ws.append(["Nome", "Confirmação"])

        # Linhas com dados
        for g in guests:
            confirm = "Confirmado" if g.confirm else "Não vai"
            ws.append([g.name, confirm])

        # Criar resposta
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = 'attachment; filename="confirmacoes.xlsx"'

        # Salvar no response
        wb.save(response)
        return response

    return render(request, "confirmations.html", {"guests": guests})

@login_required
def guests(request):
    guest_list = models.Guests.objects.all()
    return render(request, "guests.html", {"guests": guest_list})
    
def add_guests(request):
    if request.method == "POST":
        IoBytes = request.FILES.get('file').file

        if models.Guests.import_guests(IoBytes):
            return redirect("guests")
    
    return render(request, "add_guests.html")

def gift_list(request):
    gifts = models.Gift.objects.all()

    return render(request, "gift_list.html", {"gifts": gifts})

def gift(request, gift_id):
    gift = get_object_or_404(models.Gift, pk=gift_id)
    
    if request.method == "POST":
        gift.taken = True
        return redirect("success")  # ou alguma tela de agradecimento

    return render(request, "gift.html", {"gift": gift})

def edit_gift(request, gift_id):
    gift = get_object_or_404(models.Gift, pk=gift_id)
    
    if request.method == "POST":
        form = forms.GiftForm(request.POST, instance=gift)
        if form.is_valid():
            gift.save()
            return redirect("gift") 
    else:
        form = forms.GiftForm(instance=gift)

    return render(request, "edit_gift.html", {"form": form, "gift": gift})

def delete_gift(request, gift_id):
    gift = get_object_or_404(models.Gift, pk=gift_id)
    
    if request.method == "POST":
        gift.delete()
        messages.success(request, "Presente Excluído")
        return redirect("gift_list")

def add_gift(request):
    if request.method == "POST":
        form = forms.GiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gift_list")
        else:
            #TODO notificação de erro js na tela
            print(form.errors)
    else:
        form = forms.GiftForm()
    
    return render(request, "add_gift.html", {"form": form})

def import_gifts(request):
    if request.method == "POST":
        IoBytes = request.FILES.get('file').file

        if models.Gift.import_gifts(IoBytes):
            return redirect("gift_list")
    
    return render(request, "import_gifts.html")
