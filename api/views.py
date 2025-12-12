from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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

