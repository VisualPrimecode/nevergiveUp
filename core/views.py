from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreatioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Categoria, Publicacion

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





