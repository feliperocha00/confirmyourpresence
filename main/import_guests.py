import csv
from .models import Guests

def import_guests(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            name = line['nome']
            phone = line['telefone']

            if not Guests.objects.filter(name=name, phone=phone).exists():
                Guests.objects.create(name=name, phone=phone)