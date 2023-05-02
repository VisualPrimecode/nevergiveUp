from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreatioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Categoria, Publicacion
from .forms import PublicacionForm,form_Publicacion
# Create your views here.      
def MenuPrincipal(request):
    return render(request,'core/menuPrincipal.html')

def RecuperarClave(request):
    return render(request,'core/RecuperarClave.html')

def publicaciones_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    publicaciones = Publicacion.objects.filter(categoria=categoria).order_by('-fecha_creacion')
    return render(request, 'foro/publicaciones_por_categoria.html', {'categoria': categoria, 'publicaciones': publicaciones})

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


def form_Publicacion(request):
    datos = {
        'form':form_Publicacion()
    }
    if request.method=='POST':
        formulario=form_Publicacion(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardado correctamente"
    return render(request,'core/form_Publicacion.html',datos)  

from django.contrib.auth.decorators import login_required
@login_required
def crear_publicacion(request):
    categorias = Categoria.objects.all()
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

def listadoPublicaciones(request):
    Publicaciones = Publicacion.objects.all()
    contexto={"Publicaciones":Publicaciones}
    return render(request,'core/listadoPublicaciones.html',contexto)

      


