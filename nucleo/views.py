from django.shortcuts import render
from .models import Colaborador

def home(req):
    colaboradores = Colaborador .objects.all()
    print(f'Colaboradores: {colaboradores}')
    return render(req, 'nucleo/index.html')