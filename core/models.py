from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.contenido
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre