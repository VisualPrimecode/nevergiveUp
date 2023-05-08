from django.urls import path
from rest_api.views import vista_user_mod,vista_categorias_mod,vista_respuestas_mod,lista_respuestas,lista_publicaciones,lista_usuarios,vista_publicacion_mod,lista_categorias
from rest_api.viewsLogin import login
urlpatterns = [
    path('lista_publicaciones/',lista_publicaciones,name="lista_Publicaciones"),
    path('lista_usuarios/',lista_usuarios,name="lista_usuarios"),
    path('datos_publicacion/<id>',vista_publicacion_mod,name="modif_publicacion"),
    path('datos_respuestas/<id>',vista_respuestas_mod,name="vista_respuestas_mod"),
    path('datos_categorias/<id>',vista_categorias_mod,name="vista_categorias_mod"),
    path('datos_usuario/<id>',vista_user_mod,name="vista_user_mod"),
    path('lista_categorias/',lista_categorias, name="lista_categorias"), 
    path('lista_respuestas/',lista_respuestas, name="lista_respuestas"), 
    # si se activa este path se activa el login para obtner el token de algun usuario
    # y asi poder operar la api ya que se le agego la seguridad por esta via por ende
    # necesita una verificacion para ser utlizada
    #path('login/',login,name="login"),
    
]

