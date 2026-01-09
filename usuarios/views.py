from rest_framework import viewsets, filters
from usuarios.models import Paciente, Consulta, Exame
from usuarios.serializers import PacienteSerializer, ConsultaSerializer, ExameSerializer
from .permissions import IsMedico
from rest_framework.permissions import IsAuthenticated

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["nome", "cpf", "email"]


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["paciente__nome", "profissional__nome", "status", "tipo"]


class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["paciente__nome", "descricao"]
    permission_classes = [IsAuthenticated, IsMedico]