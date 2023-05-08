from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Publicacion,Categoria,Respuesta
from django.contrib.auth.models import User
from .serializers import CategoriasSerializer,RespuestasSerializer,ListacategoriaSerializers,PublicacionSerializer,listapublicacionSerializers,UserSerializers,listarespuestaSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_publicaciones(request):
    if request.method == 'GET':
        publicacion = Publicacion.objects.all()
        serializer = listapublicacionSerializers(publicacion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer = listapublicacionSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_usuarios(request):
    if request.method == 'GET':
        usuario = User.objects.all()
        serializer = UserSerializers(usuario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer = UserSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_categorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = ListacategoriaSerializers(categorias, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer = ListacategoriaSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_respuestas(request):
    if request.method == 'GET':
        respuestas = Respuesta.objects.all()
        serializer = listarespuestaSerializers(respuestas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer = listarespuestaSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_respuestas_mod(request,id):
    try:
        p = Respuesta.objects.get(id=id)
    except Respuesta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RespuestasSerializer(p)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RespuestasSerializer(p, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        p.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_publicacion_mod(request,id):
    try:
        p = Publicacion.objects.get(id=id)
    except Publicacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PublicacionSerializer(p)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PublicacionSerializer(p, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        p.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_categorias_mod(request,id):
    try:
        p = Categoria.objects.get(id=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategoriasSerializer(p)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoriasSerializer(p, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        p.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_user_mod(request,id):
    try:
        p = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializers(p)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializers(p, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        p.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)