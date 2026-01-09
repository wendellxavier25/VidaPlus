from rest_framework import serializers
from .models import Leito, Internacao, RelatorioFinanceiro, Suprimento, UnidadeSaude


class UnidadeSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeSaude
        fields = '__all__'

class LeitoSerializer(serializers.ModelSerializer):
    unidade_nome = serializers.ReadOnlyField(source="unidade.nome")

    def validate_status(self, value):
        if self.instance and self.instance.status == "ocupado" and value == "livre":
            pass 
        return value
    class Meta:
        model = Leito
        fields = "__all__"

class InternacaoSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.ReadOnlyField(source="paciente.nome")  
    leito_numero = serializers.ReadOnlyField(source="leito.numero")

    class Meta:
        model = Internacao
        fields = ['id', 'paciente', 'paciente_nome', 'leito', 'leito_numero', 'data_entrada', 'data_saida']
        extra_kwargs = {
            'data_saida': {'required': False, 'allow_null': True}
        }

class RelatorioFinanceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioFinanceiro
        fields = '__all__'


class SuprimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suprimento
        fields = '__all__'