from rest_framework import serializers
from .models import Profissional, Agenda, Prescricao

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = "__all__"

class AgendaSerializer(serializers.ModelSerializer):
    profissional_nome = serializers.CharField(source='profissional.nome', read_only=True)

    class Meta:
        model = Agenda
        fields = "__all__"

class PrescricaoSerializer(serializers.ModelSerializer):
    profissional_nome = serializers.ReadOnlyField(source="profissional.nome")
    consulta_id = serializers.ReadOnlyField(source="consulta.id")

    class Meta:
        model = Prescricao
        fields = "__all__"