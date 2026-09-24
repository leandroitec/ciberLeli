from django.utils import timezone
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
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

    #finalizar sesion y liberar pc
    @action(detail=True, methods=['get', 'post'], url_path='finalizar')
    def finalizar_sesion(self, request, pk=None):
        sesion = self.get_object()

        if sesion.fin is not None:
            return Response(
                {"error": "Esta sesión ya fue finalizada previamente."},
                status=status.HTTP_400_BAD_REQUEST
            )

        sesion.fin = timezone.now()
        sesion.pagado = True
        sesion.save()

        pc = sesion.computadora
        pc.estado = 'disponible'
        pc.save()

        return Response(
            {
                "mensaje": f"Sesión {sesion.id} finalizada con éxito. PC {pc.numero} liberada.",
                "fin": sesion.fin,
                "pagado": sesion.pagado
            },
            status=status.HTTP_200_OK
        )