from django.shortcuts import render, redirect
from .models import Juego, Plataforma
from .forms import PlataformaForm

# Create your views here.
def index(request):
    juegos = Juego.objects.all()
    return render(request, 'index.html', {
        'juegos': juegos
    })

def new_platform(request):
    if request.method == 'POST':
        platform_form = PlataformaForm(request.POST)
        if platform_form.is_valid():
            platform_form.save()
            return redirect('platform_list')
    else:
        platform_form = PlataformaForm()

    return render(request, 'new_platform.html', {'platform_form': platform_form})

def platform_list(request):
    platforms = Plataforma.objects.all()
    return render(request, 'platform_list.html', {
        'platforms': platforms
    })