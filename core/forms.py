from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Publicacion, Categoria

# class UsuarioForm(forms.ModelForm):

class CustomUserCreatioForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["username" , "first_name" , "last_name" , "email" , "password1" , "password2"]

class PublicacionForm(forms.ModelForm):
    class Meta:
        model= Publicacion
        fields = ['titulo', 'contenido', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form.control'}),
            'contenido': forms.Textarea(attrs={'class': 'form.control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
        }
from django.forms import ModelForm       

class form_publicacion(ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'categoria','autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'contenido': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
        }
    
   
