from django.urls import path, include
from .views import form_Respuesta,publicaciones_json,form_del_Publicacion,lista_mod_Publicaciones,form_mod_Publicacion,form_Publicacion,MenuPrincipal,registro,RecuperarClave,publicaciones_por_categoria,crear_publicacion,listadoPublicaciones
urlpatterns = [
    path('',MenuPrincipal, name="menuPrincipal"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',registro, name="registro"),
    path('form_Publicacion/',form_Publicacion, name="form_Publicacion"),
    path('form_Respuesta/',form_Respuesta, name="form_Respuesta"),
    path('form_mod_Publicacion/<aux_id>',form_mod_Publicacion, name="form_mod_Publicacion"),
    path('form_del_Publicacion/<aux_id>',form_del_Publicacion, name="form_del_Publicacion"),
    path('lista_mod_Publicaciones/',lista_mod_Publicaciones, name="lista_mod_Publicaciones"),
    path('RecuperarClave/',RecuperarClave, name="RecuperarClave"),
    path('publicaciones_por_categoria/<int:categoria_id>/',publicaciones_por_categoria, name="publicaciones_por_categoria"),
    path('listadoPublicaciones/',listadoPublicaciones,name="listadoPublicaciones"),
    path('crear_publicacion/',crear_publicacion, name='crear_publicacion'),
    path('publicaciones/json/', publicaciones_json, name='publicaciones_json'),
]