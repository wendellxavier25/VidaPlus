from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Paciente, Exame, Consulta

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"
        read_only_fields = ["id", "created_at"]



class ExameSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    
    class Meta:
        model = Exame
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        validated_data.setdefault("arquivos", [])
        return super().create(validated_data)

class ConsultaSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    profissional = serializers.StringRelatedField()
    
    class Meta:
        model = Consulta
        fields = "__all__"
        read_only_fields = ["id", "created_at"]