from django.urls import path, include
from .views import form_Publicacion,MenuPrincipal,registro,RecuperarClave,publicaciones_por_categoria,crear_publicacion,listadoPublicaciones
urlpatterns = [
    path('',MenuPrincipal, name="menuPrincipal"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',registro, name="registro"),
    path('form_Publicacion/',form_Publicacion, name="form_Publicacion"),
    path('RecuperarClave/',RecuperarClave, name="RecuperarClave"),
    path('publicaciones_por_categoria/<int:categoria_id>/',publicaciones_por_categoria, name="publicaciones_por_categoria"),
    path('listadoPublicaciones/',listadoPublicaciones,name="listadoPublicaciones"),
    path('crear_publicacion/',crear_publicacion, name='crear_publicacion'),
]