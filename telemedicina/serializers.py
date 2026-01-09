from rest_framework import serializers
from .models import TeleConsulta, Prontuario


class TeleConsultaSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    profissional_nome = serializers.CharField(source="profissional.nome", read_only=True)

    class Meta:
        model = TeleConsulta
        fields = "__all__"


class ProntuarioSerializer(serializers.ModelSerializer):
    consulta_info = serializers.CharField(source="consulta.id", read_only=True)

    class Meta:
        model = Prontuario
        fields = "__all__"
