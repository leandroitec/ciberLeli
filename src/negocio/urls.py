from django.urls import path
from . import views

urlpatterns = [
    path('computadoras/', views.computadoras_list, name='computadoras_list'),
    path('computadoras/<int:pk>/', views.computadora_detail, name='computadora_detail'),
    path('sesiones/', views.sesiones_list, name='sesiones_list'),
    path('sesiones/<int:pk>/', views.sesion_detail, name='sesion_detail'),
]