from django.shortcuts import render, redirect
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm

# Vista para listar parroquias con sus barrios
def parroquias_y_barrios(request):
    parroquias = Parroquia.objects.all()
    return render(request, 'parroquias_y_barrios.html', {'parroquias': parroquias})

# Vista para listar todos los barrios
def lista_barrios(request):
    barrios = Barrio.objects.all()
    return render(request, 'lista_barrios.html', {'barrios': barrios})

# Vista para crear una nueva parroquia
def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parroquias_y_barrios')
    else:
        form = ParroquiaForm()
    return render(request, 'crear_parroquia.html', {'form': form})

# Vista para crear un nuevo barrio
def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_barrios')
    else:
        form = BarrioForm()
    return render(request, 'crear_barrio.html', {'form': form})

def index(request):
    return render(request, 'index.html')

