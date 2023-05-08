from django.shortcuts import render, redirect
from .forms import CustomUserCreatioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Categoria, Publicacion,Respuesta
from .forms import PublicacionForm,form_publicacion,form_respuesta,form_categoria
from django.contrib.auth.decorators import login_required
# Create your views here.      
def MenuPrincipal(request):
    return render(request,'core/menuPrincipal.html')

def RecuperarClave(request):
    return render(request,'core/RecuperarClave.html')

def registro(request):
    data={
        'form':CustomUserCreatioForm()
    }
    if request.method=='POST':
        formulario = CustomUserCreatioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"te has registrado correctamente")
            return redirect('menuPrincipal')
        data["form"]=formulario
    return render(request, 'registration/registro.html',data)

@login_required
def form_Publicacion(request):
    datos = {
        'form':form_publicacion()
    }
    if request.method=='POST':
        formulario=form_publicacion(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardado correctamente"
    return render(request,'core/form_Publicacion.html',datos)

@login_required
def form_Categoria(request):
    datos = {
        'form':form_categoria()
    }
    if request.method=='POST':
        formulario=form_categoria(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardado correctamente"
    return render(request,'core/form_Categoria.html',datos)    

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            messages.success(request,'Publicación creada con éxito.')
            return redirect('menuPrincipal')
    else:
        form = PublicacionForm()
    return render(request, 'core/crear_publicacion.html', {'form': form})


def form_mod_Publicacion(request, aux_id):
    pub = Publicacion.objects.get(id=aux_id)
    datos = {
        'form':form_publicacion(instance=pub)
    }
    if request.method=='POST':
        formulario=form_publicacion(data=request.POST, instance=pub)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificado correctamente"
    return render(request, 'core/form_mod_Publicacion.html',datos)

def form_mod_Categoria(request, aux_id):
    ctg = Categoria.objects.get(id=aux_id)
    datos = {
        'form':form_categoria(instance=ctg)
    }
    if request.method=='POST':
        formulario=form_categoria(data=request.POST, instance=ctg)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificado correctamente"
    return render(request, 'core/form_mod_Categoria.html',datos)

def form_mod_Respuesta(request, aux_id):
    rsp = Respuesta.objects.get(id=aux_id)
    datos = {
        'form':form_respuesta(instance=rsp)
    }
    if request.method=='POST':
        formulario=form_respuesta(data=request.POST, instance=rsp)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificado correctamente"
    return render(request, 'core/form_mod_Respuesta.html',datos)

def lista_mod_Publicaciones(request):
    publicaciones = Publicacion.objects.all()
    datos = {
        "publicaciones":publicaciones
    }
    return render(request,'core/lista_mod_Publicaciones.html',datos)
def lista_mod_Categorias(request):
    ctg = Categoria.objects.all()
    datos = {
        "categorias":ctg
    }
    return render(request,'core/lista_mod_Categorias.html',datos)
def lista_mod_Respuestas(request):
    rsp = Respuesta.objects.all()
    datos = {
        "respuestas":rsp
    }
    return render(request,'core/lista_mod_Respuestas.html',datos)

def form_del_Publicacion(request, aux_id):
    publi = Publicacion.objects.get(id=aux_id)
    datos = {
        'form':form_publicacion(instance=publi)
    }
    if request.method=='POST':
        formulario= form_publicacion(data=request.POST, instance=publi)
        publi.delete()
        datos['mensaje']="Eliminado correctamente"
    return render(request,'core/form_del_Publicacion.html',datos)

def form_del_Categoria(request, aux_id):
    catg = Categoria.objects.get(id=aux_id)
    datos = {
        'form':form_categoria(instance=catg)
    }
    if request.method=='POST':
        formulario= form_categoria(data=request.POST, instance=catg)
        catg.delete()
        datos['mensaje']="Categoria Eliminada correctamente"
        
    return render(request,'core/form_del_Categoria.html',datos)

def form_del_Respuesta(request, aux_id):
    rsp = Respuesta.objects.get(id=aux_id)
    datos = {
        'form':form_respuesta(instance=rsp)
    }
    if request.method=='POST':
        formulario= form_respuesta(data=request.POST, instance=rsp)
        rsp.delete()
        datos['mensaje']="Respuesta Eliminada correctamente"
        
    return render(request,'core/form_del_Respuesta.html',datos)

from django.core import serializers
from django.http import HttpResponse


def publicaciones_json():
    publicaciones = Publicacion.objects.all()
    publicaciones_json = serializers.serialize('json', publicaciones)
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="publicaciones.json"'
    response.write(publicaciones_json)

    return response

@login_required
def form_Respuesta(request):
    datos = {
        'form':form_respuesta()
    }
    if request.method=='POST':
        formulario=form_respuesta(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardado correctamente"
    return render(request,'core/form_Respuesta.html',datos)  

def info_publicacion(request, publicacion_id):
    # Obtenemos la publicación y sus respuestas asociadas
    publicacionaux = Publicacion.objects.get(id=publicacion_id)
    respuestas = Respuesta.objects.filter(publicacion=publicacionaux)

    # Creamos un contexto con los datos de la publicación y sus respuestas
    context = {
        'publicacion': publicacionaux,
        'respuestas': respuestas,
    }

    # Renderizamos la plantilla HTML con el contexto
    return render(request, 'info_publicacion.html', context)

      


