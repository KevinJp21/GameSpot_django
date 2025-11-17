from django.shortcuts import render, redirect
from .models import Juego, Plataforma, Genero, Desarrollador
from .forms import PlataformaForm, GeneroForm, DesarrolladorForm, GameForm

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

#CRUD de Desarrolladores
def new_developer(request):
    if request.method == 'POST':
        developer_form = DesarrolladorForm(request.POST)
        if developer_form.is_valid():
            developer_form.save()
            return redirect('developer_list')
    else:
        developer_form = DesarrolladorForm()

    return render(request, 'developers/new_developer.html', {'developer_form': developer_form})

def developer_list(request):
    developers = Desarrollador.objects.all()

    return render(request, 'developers/developer_list.html', {
        'developers': developers
    })

def update_developer(request, id):
    developer = Desarrollador.objects.get(id=id)

    if request.method == 'POST':
        developer_form = DesarrolladorForm(request.POST, instance=developer)
        if developer_form.is_valid():
            developer_form.save()
            return redirect('developer_list')
    else:
        developer_form = DesarrolladorForm(instance=developer)

    return render(request, 'developers/update_developer.html', {'developer_form': developer_form})

def delete_developer(request, id):
    developer_form = Desarrollador.objects.get(id=id)

    if request.method == 'POST':
        developer_form.delete()
        return redirect('developer_list')

    return render(request, 'developers/delete_developer.html', {'developer_form': developer_form})

#CRUD de Juegos
def new_game(request):
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        if game_form.is_valid():
            game_form.save()
            return redirect('game_list')
    else:
        game_form = GameForm()

    return render(request, 'games/new_game.html', {'game_form': game_form})

def game_list(request):
    games = Juego.objects.all()

    return render(request, 'games/game_list.html', {
        'games': games
    })

def update_game(request, id):
    game_form = Juego.objects.get(id=id)

    if request.method == 'POST':
        game_form = GameForm(request.POST, instance=game_form)
        if game_form.is_valid():
            game_form.save()
            return redirect('game_list')
    else:
        game_form = GameForm(instance=game_form)

    return render(request, 'games/update_game.html', {'game_form': game_form})

def delete_game(request, id):
    game_form = Juego.objects.get(id=id)

    if request.method == 'POST':
        game_form.delete()
        return redirect('game_list')

    return render(request, 'games/delete_game.html', {'game_form': game_form})