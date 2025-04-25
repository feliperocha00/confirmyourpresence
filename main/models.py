from django.db import models
from django.core.validators import RegexValidator
import re
import csv

class Welcome(models.Model):
    def find_number(self, phone):
        phone = re.sub(r'\D', '', phone)
        if Guests.objects.filter(phone=phone).exists():
            return True
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

    def __str__(self):
        return self.name
           
    def import_guests(file):
        with open(file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                name = line['Nome']
                phone = line['Telefone']
                phone = re.sub(r'\D', '', phone)
                parent = line['Pai']
                parent = Guests.objects.filter(name=parent).first() if parent else None

                if not Guests.objects.filter(name=name, phone=phone).exists():
                    Guests.objects.create(name=name, phone=phone, parent=parent)

class Confirm(models.Model):
    name = models.CharField("Nome", max_length=200)
    confirm = models.BooleanField("Confirma sua Presença?")

    def is_valid(self):
        if self:
            return True
        else:
            return False

    def __str__(self):
        return self.name
    
class Confirmations(models.Model):
    def export(self, confirmations):
        print("Exportando confirmações...")
        return True
