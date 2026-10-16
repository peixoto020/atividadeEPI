from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .models import Colaborador
from .forms import ColaboradorForm

def home(req):
    colaboradores = Colaborador .objects.all()
    print(f'Colaboradores: {colaboradores}')
    return render(req, 'nucleo/index.html', {'colaboradores': colaboradores})

def criar_colaborador(req):
    form = ColaboradorForm(req.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home') # Redireciona para a tela inicial após salvar
    return render(req, 'nucleo/form.html', {'form': form})


def editar_colaborador(req, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    form = ColaboradorForm(req.POST or None, instance=colaborador)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(req, 'nucleo/form.html', {'form': form, 'colaborador': colaborador})


def excluir_colaborador(req, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if req.method == 'POST':
        colaborador.delete()
        return redirect('home')
    return render(req, 'nucleo/confirm_delete.html', {'colaborador': colaborador})