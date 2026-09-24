from rest_framework.routers import DefaultRouter
from .views import ComputadoraViewSet, TarifaViewSet, JuegoViewSet, SesionUsoViewSet

router = DefaultRouter()
router.register(r'computadoras', ComputadoraViewSet, basename='computadora')
router.register(r'tarifas', TarifaViewSet, basename='tarifa')
router.register(r'juegos', JuegoViewSet, basename='juego')
router.register(r'sesiones', SesionUsoViewSet, basename='sesion')