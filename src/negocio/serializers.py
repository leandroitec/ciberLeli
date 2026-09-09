from rest_framework import serializers
from .models import Computadora, SesionUso, Tarifa, Juego

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = '__all__'
   
class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__'

class ComputadoraSerializer(serializers.ModelSerializer):
    juegos = JuegoSerializer(many=True, read_only=True) 

    class Meta:
        model = Computadora
        fields = ['id', 'numero', 'nombre', 'estado', 'especificaciones', 'juegos']

class SesionUsoSerializer(serializers.ModelSerializer):
    computadora_detalle = ComputadoraSerializer(source='computadora', read_only=True)
    # para mostrar detalles
    class Meta:
        model = SesionUso
        fields = '__all__'
        