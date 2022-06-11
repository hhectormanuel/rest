from urllib import response
from rest_framework.views import APIView
from .serializer import UsuarioSerializer
from .models import Usuario
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserAPIView(APIView):

    def get(self, request):
        usuarios = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuarios, many=True)
        return Response(usuario_serializer.data)

@api_view(['GET', 'POST'])
def get(request):

    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuarios, many=True)
        return Response(usuario_serializer.data)

    elif request.method == 'POST':
        usuario_serializer = UsuarioSerializer(data = request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return response(usuario_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk=None):
    if request.method == 'GET':
        usuario = Usuario.objects.get(id = pk)
        usuario_serializer = UsuarioSerializer(usuario)
        return Response(usuario_serializer.data)

    elif request.method == 'PUT':
        usuario = Usuario.objects.get(id = pk)
        usuario_serializer = UsuarioSerializer(usuario, data= request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return response(usuario_serializer.errors)

    elif request.method == 'DELETE':
        usuario = Usuario.objects.get(id = pk)
        usuario.delete()
        return Response('Eliminado')