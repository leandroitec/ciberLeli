from rest_framework import generics
from .models import Computadora, SesionUso, Tarifa, Juego
from .serializers import (
    ComputadoraSerializer,
    SesionUsoSerializer,
    TarifaSerializer,
    JuegoSerializer,
)

class ComputadoraListCreateView(generics.ListCreateAPIView):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer

class ComputadoraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer


class JuegoListCreateView(generics.ListCreateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

class JuegoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer


class TarifaListCreateView(generics.ListCreateAPIView):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer

class TarifaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer

class SesionUsoListCreateView(generics.ListCreateAPIView):
    queryset = SesionUso.objects.all().order_by('-inicio')
    serializer_class = SesionUsoSerializer

    def perform_create(self, serializer):
        sesion = serializer.save()
        pc = sesion.computadora
        pc.estado = 'ocupada'
        pc.save()

class SesionUsoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SesionUso.objects.all()
    serializer_class = SesionUsoSerializer

    def perform_update(self, serializer):
        sesion = serializer.save()
        if sesion.fin or sesion.pagado:
            pc = sesion.computadora
            pc.estado = 'disponible'
            pc.save()

    def perform_destroy(self, instance):
        pc = instance.computadora
        pc.estado = 'disponible'
        pc.save()
        instance.delete()