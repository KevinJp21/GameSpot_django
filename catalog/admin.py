from django.contrib import admin
from .models import Plataforma, Genero, Desarrollador, Juego
# Register your models here.

admin.site.register(Plataforma)
admin.site.register(Genero)
admin.site.register(Desarrollador)
admin.site.register(Juego)