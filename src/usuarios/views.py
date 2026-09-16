from rest_framework import generics
from .serializers import UsuariosSerializer
from .models import UsuarioPersonalizado

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuariosSerializer


class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuariosSerializer

        
"""
{ "username" : "leli" ,
"email": "leandro@gmail.com" ,
"dni": "45592159" ,
"telefono": "3583417514"} 
"""        
