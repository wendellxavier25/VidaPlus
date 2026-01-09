from rest_framework.viewsets import ModelViewSet
from .models import Profissional, Agenda
from .serializers import ProfissionalSerializer, AgendaSerializer

class ProfissionalViewSet(ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class AgendaViewSet(ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer