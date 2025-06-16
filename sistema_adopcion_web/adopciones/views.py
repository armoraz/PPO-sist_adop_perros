from django.shortcuts import render, redirect
from .models import Perro
from .forms import UsuarioAdoptanteForm

def lista_perros(request):
    perros = Perro.objects.filter(estado='disponible')
    return render(request, 'lista_perros.html', {'perros': perros})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioAdoptanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_perros')
    else:
        form = UsuarioAdoptanteForm()
    return render(request, 'registrar_usuario.html', {'form': form})