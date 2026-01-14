from rest_framework.permissions import BasePermission

class IsMedico(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.groups.filter(name="Medico").exists()
        )


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.perfil == "admin"
        )


class IsPaciente(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.perfil == "paciente"
        )