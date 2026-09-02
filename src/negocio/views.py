from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Computadora, SesionUso
from .serializers import ComputadoraSerializer, SesionUsoSerializer

@api_view(["GET", "POST"])
def computadoras_list(request):
    if request.method == "GET":
        pcs = Computadora.objects.all()
        serializer = ComputadoraSerializer(pcs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ComputadoraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def computadora_detail(request, pk):
    try:
        pc = Computadora.objects.get(pk=pk)
    except Computadora.DoesNotExist:
        return Response({"error": "Computadora no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ComputadoraSerializer(pc)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = ComputadoraSerializer(pc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        pc.delete()
        return Response({"mensaje": "Computadora eliminada"}, status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(["GET", "POST"])
def sesiones_list(request):
    if request.method == "GET":
        sesiones = SesionUso.objects.all().order_by('-inicio')
        serializer = SesionUsoSerializer(sesiones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = SesionUsoSerializer(data=request.data)
        if serializer.is_valid():
            sesion = serializer.save()
            # cambia automáticamente el estado de la PC a ocupada
            pc = sesion.computadora
            pc.estado = 'ocupada'
            pc.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""
{
  "usuario": 1,
  "computadora": 1,
  "tiempo_solicitado_minutos": 60,
  "pagado": false,
  "total_a_pagar": "1500.00"
}
"""

@api_view(["GET", "PUT", "DELETE"])
def sesion_detail(request, pk):
    try:
        sesion = SesionUso.objects.get(pk=pk)
    except SesionUso.DoesNotExist:
        return Response({"error": "Sesión no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SesionUsoSerializer(sesion)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = SesionUsoSerializer(sesion, data=request.data, partial=True)
        if serializer.is_valid():
            sesion_actualizada = serializer.save()
            
            # libera la PC si se marca la fecha de fin o se paga
            if sesion_actualizada.fin or sesion_actualizada.pagado:
                pc = sesion_actualizada.computadora
                pc.estado = 'disponible'
                pc.save()
                
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # liberamos la computadora al cancelar la sesion 
        pc = sesion.computadora
        pc.estado = 'disponible'
        pc.save()
        sesion.delete()
        return Response({"mensaje": "Sesión eliminada"}, status=status.HTTP_204_NO_CONTENT)

