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
    name = models.CharField("Produto", max_length=200)
    price = models.FloatField("Preço")
    image = models.BinaryField(null=True)
    
    def find_gift(self, gift_id):
        gift = Gift.objects.filter(id=gift_id).first()
        return gift

    def buy(self):
        return True
    
# class Cart(models.Model):
    # product_ids = models.ManyToManyRel() TODO relation with products