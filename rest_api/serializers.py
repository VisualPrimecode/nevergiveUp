from rest_framework import serializers
from core.models import Respuesta,Publicacion
from django.contrib.auth.models import User
from django import forms

# class UsuarioForm(forms.ModelForm):

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username' , 'first_name' , 'last_name', 'email' , 'password']

class form_publicacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'categoria','autor']

class form_respuestaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ['contenido','autor','publicacion']
class PublicacionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publicacion
        fields = ['id', 'titulo', 'contenido', 'fecha_creacion', 'autor', 'categoria']