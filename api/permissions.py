from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnlyByGroup(BasePermission):
    """
    - Admin group: puede crear/editar/eliminar
    - Otros autenticados: solo lectura (GET, HEAD, OPTIONS)
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Admin").exists()
        )
