from django.shortcuts import render, redirect
from .models import Juego, Plataforma, Genero
from .forms import PlataformaForm, GeneroForm

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

#CRUD de Generos
def new_genre(request):
    if request.method == 'POST':
        genre_form = GeneroForm(request.POST)
        if genre_form.is_valid():
            genre_form.save()
            return redirect('genre_list')
    else:
        genre_form = GeneroForm()

    return render(request, 'genres/new_genre.html', {'genre_form': genre_form})

def genre_list(request):
    genres = Genero.objects.all()

    return render(request, 'genres/genre_list.html', {
        'genres': genres
    })

def update_genre(request, id):
    genre = Genero.objects.get(id=id)

    if request.method == 'POST':
        genre_form = GeneroForm(request.POST, instance=genre)
        if genre_form.is_valid():
            genre_form.save()
            return redirect('genre_list')
    else:
        genre_form = GeneroForm(instance=genre)

    return render(request, 'genres/update_genre.html', {'genre_form': genre_form})

def delete_genre(request, id):
    genre_form = Genero.objects.get(id=id)
    
    if request.method == 'POST':
        genre_form.delete()
        return redirect('genre_list')

    return render(request, 'genres/delete_genre.html', {'genre_form': genre_form})