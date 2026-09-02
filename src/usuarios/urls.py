from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.users, name='users_list'),
    path('usuarios/<int:pk>/', views.user_detail, name='user_detail'),
]