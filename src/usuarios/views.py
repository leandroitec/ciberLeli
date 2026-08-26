from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UsuarioPersonalizadoForm

@api_view(["GET","POST"])
def registro_usuario(request):
    return Response({"hola":"mundo"}, status=status.HTTP_200_OK)
