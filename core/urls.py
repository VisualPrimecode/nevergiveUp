from django.urls import path, include
from .views import info_publicacion,lista_mod_Respuestas,form_mod_Respuesta,form_del_Respuesta,lista_mod_Categorias,form_mod_Categoria,form_del_Categoria,form_Respuesta,publicaciones_json,form_del_Publicacion,lista_mod_Publicaciones,form_mod_Publicacion,form_Publicacion,MenuPrincipal,registro,RecuperarClave,form_Categoria


urlpatterns = [
    path('',MenuPrincipal, name="menuPrincipal"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',registro, name="registro"),
    path('form_Publi',form_Publicacion, name="form_Publicacion"),
    path('form_Categoria/',form_Categoria, name="form_Categoria"),
    path('form_Respuesta/',form_Respuesta, name="form_Respuesta"),
    #no pudimos hacer correr este.
    path('info_publicacion/<publicacion_id>',info_publicacion, name="info_publicacion"),
    path('form_mod_Publicacion/<aux_id>',form_mod_Publicacion, name="form_mod_Publicacion"),
    path('form_mod_Categoria/<aux_id>',form_mod_Categoria, name="form_mod_Categoria"),
    path('form_mod_Respuesta/<aux_id>',form_mod_Respuesta, name="form_mod_Respuesta"),
    path('form_del_Publicacion/<aux_id>',form_del_Publicacion, name="form_del_Publicacion"),
    path('form_del_Respuesta/<aux_id>',form_del_Respuesta, name="form_del_Respuesta"),
    path('form_del_Categoria/<aux_id>',form_del_Categoria, name="form_del_Categoria"),
    path('form_del_Respuesta/<aux_id>',form_del_Respuesta, name="form_del_Respuesta"),
    path('lista_mod_Publicaciones/',lista_mod_Publicaciones, name="lista_mod_Publicaciones"),
    path('lista_mod_Categorias/',lista_mod_Categorias, name="lista_mod_Categorias"),
    path('lista_mod_Respuestas/',lista_mod_Respuestas, name="lista_mod_Respuestas"),
    path('RecuperarClave/',RecuperarClave, name="RecuperarClave"),
    path('publicaciones/json/', publicaciones_json, name='publicaciones_json'),
]