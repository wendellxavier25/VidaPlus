from rest_framework import viewsets
from .models import TeleConsulta, Prontuario
from .serializers import TeleConsultaSerializer, ProntuarioSerializer

class TeleConsultaViewSet(viewsets.ModelViewSet):
    queryset = TeleConsulta.objects.all()
    serializer_class = TeleConsultaSerializer

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
