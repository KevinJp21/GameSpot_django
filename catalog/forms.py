from dataclasses import field
from django import forms
from .models import Plataforma, Genero, Desarrollador, Juego

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'