from django.urls import path
from rest_api.views import lista_Publicaciones,lista_usuarios,vista_publicacion_mod
from rest_api.viewsLogin import login
urlpatterns = [
    path('lista_Publicaciones/',lista_Publicaciones,name="lista_Publicaciones"),
    path('lista_usuarios/',lista_usuarios,name="lista_usuarios"),
    path('datos_publicacion/<id>',vista_publicacion_mod,name="modif_publicacion"),
    path('login/',login,name="login"),
    
]

