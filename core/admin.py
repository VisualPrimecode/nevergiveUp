from django.contrib import admin
from .models import Publicacion,Respuesta,Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Respuesta)
admin.site.register(Publicacion)