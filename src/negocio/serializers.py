from rest_framework import serializers
from .models import Computadora, SesionUso, Tarifa

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = '__all__'

class ComputadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computadora
        fields = '__all__'

class SesionUsoSerializer(serializers.ModelSerializer):
    computadora_detalle = ComputadoraSerializer(source='computadora', read_only=True)
    # para mostrar detalles
    class Meta:
        model = SesionUso
        fields = '__all__'
