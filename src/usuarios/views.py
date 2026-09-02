from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UsuariosSerializer
from .models import UsuarioPersonalizado

@api_view(["GET", "POST"])
def users(request):
    if request.method == "GET":
        usuarios = UsuarioPersonalizado.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response(
                {
                    "mensaje": "Usuario creado con éxito",
                    "data": serializer.data
                }, 
                status=status.HTTP_201_CREATED
            )
            
        return Response(
                    {"mensaje": "No se creó porque no es válido"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        
"""
{ "username" : "leli" ,
"email": "leandro@gmail.com" ,
"dni": "45592159" ,
"telefono": "3583417514"} 
"""        


@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, pk):
    try:
        usuario = UsuarioPersonalizado.objects.get(pk=pk)
    except UsuarioPersonalizado.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UsuariosSerializer(usuario)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = UsuariosSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        usuario.delete()
        return Response({"mensaje": "Usuario eliminado"}, status=status.HTTP_204_NO_CONTENT)
        