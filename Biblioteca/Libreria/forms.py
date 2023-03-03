from django import forms
from .models import Autor, Libro
from django.forms.widgets import DateInput

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido','apodo','nacionalidad','correo']
        
class LibroForm(forms.ModelForm):
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), empty_label="Seleccione un autor")
    
    class Meta:
        model = Libro
        fields = ['titulo', 'descripcion', 'autor', 'fecha_publicacion']
        widgets = {
            'fecha_publicacion': DateInput(attrs={'type': 'date'})
            }
