from dataclasses import field
from django import forms
from .models import Plataforma, Genero, Desarrollador, Juego

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = '__all__'

class GameForm(forms.ModelForm):
    plataforma = forms.ModelMultipleChoiceField(queryset=Plataforma.objects.all(), widget=forms.CheckboxSelectMultiple)
    genero = forms.ModelMultipleChoiceField(queryset=Genero.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Juego
        fields = '__all__'
        widgets = {
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date'}),
        }