from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Departamento, Sensor, Evento, Barrera
from .serializers import (DepartamentoSerializer, SensorSerializer, EventoSerializer, BarreraSerializer)
from .permissions import IsAdminOrReadOnlyByGroup

@api_view(["GET"])
@permission_classes([AllowAny])
def api_info(request):
    return Response({
        "autor": ["Alejandro Tapia Paz"],
        "asignatura": "Programación Back End",
        "proyecto": "SmartConnect API",
        "descripcion": "API RESTful para administrar sensores, departamentos y eventos de acceso.",
        "version": "1.0"
    })



# tu api_info se queda arriba tal cual

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all().order_by("id")
    serializer_class = DepartamentoSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyByGroup]


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all().order_by("id")
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyByGroup]


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().order_by("-fecha_hora")
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyByGroup]


class BarreraViewSet(viewsets.ModelViewSet):
    queryset = Barrera.objects.all().order_by("id")
    serializer_class = BarreraSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyByGroup]

