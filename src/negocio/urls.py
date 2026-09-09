from django.urls import path
from . import views

urlpatterns = [
    path('computadoras/', views.ComputadoraListCreateView.as_view(), name='computadora-list-create'),
    path('computadoras/<int:pk>/', views.ComputadoraDetailView.as_view(), name='computadora-detail'),
    path('tarifas/', views.TarifaListCreateView.as_view(), name='tarifa-list-create'),
    path('tarifas/<int:pk>/', views.TarifaDetailView.as_view(), name='tarifa-detail'),
    path('sesiones/', views.SesionUsoListCreateView.as_view(), name='sesion-list-create'),
    path('sesiones/<int:pk>/', views.SesionUsoDetailView.as_view(), name='sesion-detail'),
    path('juegos/', views.JuegoListCreateView.as_view(), name='juego-list-create'),
    path('juegos/<int:pk>/', views.JuegoDetailView.as_view(), name='juego-detail'),
]