from django.db import models
from django.core.validators import RegexValidator
import re
import csv
import base64
import io

class Welcome(models.Model):
    def find_number(self, phone):
        phone = re.sub(r'\D', '', phone)
        guest = Guests.objects.filter(phone=phone).first()
        if guest:
            guest_childs = guest.childs.all()
            guests = guest_childs
            guests = list(guests)
            guests.append(guest)
            return guests
        else:
            return False

class ListVerify(models.Model):
    def find_number(self, phone):
        phone = re.sub(r'\D', '', phone)
        guest = Guests.objects.filter(phone=phone).first()
        if guest:
            guest_childs = guest.childs.all()
            guests = guest_childs
            guests = list(guests)
            guests.append(guest)
            return guests
        else:
            return False
    
class Guests(models.Model):
    name = models.CharField("Nome", max_length=12)
    phone = models.CharField(
        max_length=11,
        validators=[RegexValidator(regex=r'^\d{10,11}$', message='Digite um número de telefone válido.')]
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='childs'
    )
    confirm = models.BooleanField(
        "Confirma a presença?",
        default=False
    )

    def __str__(self):
        return self.name
           
    def import_guests(IoBytes):
        data_file = io.StringIO(IoBytes.getvalue().decode('utf-8'))
        data_file.seek(0)
        file_reader = []
        csv_reader = csv.reader(data_file, delimiter=',')
        file_reader.extend(csv_reader)

        for index, line in enumerate(file_reader):
            if index == 0:
                # Ignora o cabeçalho
                continue

            name = line[1]
            phone = line[4]
            phone = re.sub(r'\D', '', phone)
            parent = line[3]
            parent = Guests.objects.filter(name=parent).first() if parent else None

            if not Guests.objects.filter(name=name, phone=phone).exists():
                Guests.objects.create(name=name, phone=phone, parent=parent)

class Confirm(models.Model):
    name = models.CharField("Nome", max_length=200)
    confirm = models.BooleanField("Confirma sua Presença?")

    def __str__(self):
        return self.name
    
class Confirmations(models.Model):
    def export(self, confirmations):
        print("Exportando confirmações...")
        return True

class Gift(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True)
    product_url = models.URLField(max_length=500, null=True)
    taken = models.BooleanField(default=False)
    
    def find_gift(self, gift_id):
        gift = Gift.objects.filter(id=gift_id).first()
        return gift

    # def buy(self):
    #     return True
        
    def import_gifts(IoBytes):
        data_file = io.StringIO(IoBytes.getvalue().decode('utf-8'))
        data_file.seek(0)
        file_reader = []
        csv_reader = csv.reader(data_file, delimiter=',')
        file_reader.extend(csv_reader)

        for index, line in enumerate(file_reader):
            if index == 0:
                # Ignora o cabeçalho
                continue

            name = line[0]
            price = line[1]
            price_treated = re.sub(r'[^0-9.,]', '', price)
            price_treated = price_treated.replace(',', '.')
            price = float(price_treated)
            image_url = line[2]
            product_url = line[3]

            if not Gift.objects.filter(name=name).exists():
                Gift.objects.create(name=name, price=price, image_url=image_url, product_url=product_url)
