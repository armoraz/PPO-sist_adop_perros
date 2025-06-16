from django import forms
from .models import Perro, UsuarioAdoptante

class UsuarioAdoptanteForm(forms.ModelForm):
    class Meta:
        model = UsuarioAdoptante
        fields = '__all__'

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = '__all__'