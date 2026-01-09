from rest_framework import viewsets, filters
from .models import Profissional, Agenda, Prescricao
from .serializers import ProfissionalSerializer, AgendaSerializer, PrescricaoSerializer


class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["nome", "crm", "especialidade", "tipo"]


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["profissional__nome"]


class PrescricaoViewSet(viewsets.ModelViewSet):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["profissional__nome", "consulta__id"]
