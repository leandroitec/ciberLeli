from rest_framework import serializers
from .models import UsuarioPersonalizado

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['id', 'username', 'email', 'dni', 'telefono']
