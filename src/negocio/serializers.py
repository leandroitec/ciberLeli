from rest_framework import serializers
from .models import Computadora, SesionUso, Producto, VentaProducto, Tarifa

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = '__all__'

class ComputadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computadora
        fields = '__all__'

class SesionUsoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionUso
        fields = '__all__'
        # Evitamos que alteren manualmente el precio congelado desde la API externa
        read_only_fields = ['precio_tarifa_aplicado']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class VentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaProducto
        fields = '__all__'

