from django import forms
from .models import Alumno , Profesor

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['id_alumno', 'Nombres']
        widgets = {
            'id_alumno': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'Nombres': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['id_profesor', 'nombre_profesor']
        widgets = {
            'id_profesor': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'nombre_profesor': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }
