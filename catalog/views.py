from django.shortcuts import render
from .models import Juego
from .forms import PlataformaForm

# Create your views here.
def index(request):
    juegos = Juego.objects.all()
    return render(request, 'index.html', {
        'juegos': juegos
    })

def new_platform(request):
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PlataformaForm()

    context = {
        'form': form
    }
    return render(request, 'new_platform.html', context)