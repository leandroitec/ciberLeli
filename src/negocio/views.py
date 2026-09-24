from rest_framework import viewsets, permissions
from .models import Computadora, SesionUso, Tarifa, Juego
from .serializers import (
    ComputadoraSerializer,
    SesionUsoSerializer,
    TarifaSerializer,
    JuegoSerializer,
)

class TarifaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer
    permission_classes = [permissions.AllowAny]

class ComputadoraViewSet(viewsets.ModelViewSet):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SesionUsoViewSet(viewsets.ModelViewSet):
    queryset = SesionUso.objects.all().order_by('-inicio')
    serializer_class = SesionUsoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        sesion = serializer.save()
        pc = sesion.computadora
        pc.estado = 'ocupada'
        pc.save()

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