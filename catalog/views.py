from django.shortcuts import render, redirect
from .models import Juego, Plataforma
from .forms import PlataformaForm

# Create your views here.
def index(request):
    juegos = Juego.objects.all()
    return render(request, 'index.html', {
        'juegos': juegos
    })

#CRUD de Plataformas
def new_platform(request):
    if request.method == 'POST':
        platform_form = PlataformaForm(request.POST)
        if platform_form.is_valid():
            platform_form.save()
            return redirect('platform_list')
    else:
        platform_form = PlataformaForm()

    return render(request, 'platforms/new_platform.html', {'platform_form': platform_form})

def platform_list(request):
    platforms = Plataforma.objects.all()

    return render(request, 'platforms/platform_list.html', {
        'platforms': platforms
    })

def update_platform(request, id):
    platform = Plataforma.objects.get(id=id)

    if request.method == 'POST':
        platform_form = PlataformaForm(request.POST, instance=platform)
        if platform_form.is_valid():
            platform_form.save()
            return redirect('platform_list')
    else:
        platform_form = PlataformaForm(instance=platform)

    return render(request, 'platforms/update_platform.html', {'platform_form': platform_form})

def delete_platform(request, id):
    platform_form = Plataforma.objects.get(id=id)
    
    if request.method == 'POST':
        platform_form.delete()
        return redirect('platform_list')

    return render(request, 'platforms/delete_platform.html', {'platform_form': platform_form})