from rest_framework import serializers
from core.models import Respuesta,Publicacion,Categoria
from django.contrib.auth.models import User
from django import forms

# class UsuarioForm(forms.ModelForm):

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username' , 'first_name' , 'last_name', 'email' , 'password']

class listapublicacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['id','titulo', 'contenido','fecha_creacion','autor', 'categoria']

class listarespuestaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ['contenido','autor','publicacion']
             
class ListacategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = ['nombre','descripcion']
        
class RespuestasSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Respuesta
        fields = ['id','contenido', 'fecha_creacion', 'autor_id','publicacion_id']
        
class PublicacionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publicacion
        fields = ['id', 'titulo', 'contenido', 'fecha_creacion', 'autor', 'categoria']
class CategoriasSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']