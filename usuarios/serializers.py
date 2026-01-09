from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Paciente, Exame, Consulta

class PacienteSerializer(serializers.ModelSerializer):
    cpf = serializers.SerializerMethodField()

    def get_cpf(self, obj):
        return f"***.***.{obj.cpf[-3:]}"
    
    class Meta:
        model = Paciente
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ExameSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)

    class Meta:
        model = Exame
        fields = "__all__"
        read_only_fields = ["id"]


class ConsultaSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    profissional = serializers.StringRelatedField()
    
    class Meta:
        model = Consulta
        fields = "__all__"
        read_only_fields = ["id", "created_at"]