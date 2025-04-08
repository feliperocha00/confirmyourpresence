from django.db import models
from django.core.validators import RegexValidator

class Welcome(models.Model):
    def find_number(self):
        return True

class Guests(models.Model):
    name = models.CharField("Nome", max_length=12)
    phone = models.CharField(
        max_length=11,
        validators=[RegexValidator(regex=r'^\d{10,11}$', message='Digite um número de telefone válido.')]
    )
    presenca = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])

# Create your models here.
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
    