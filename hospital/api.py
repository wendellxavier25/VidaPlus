from rest_framework import viewsets
from hospital.models import Leito, Internacao, RelatorioFinanceiro, Suprimento
from hospital.serializers import (
    LeitoSerializer,
    InternacaoSerializer,
    RelatorioFinanceiroSerializer,
    SuprimentoSerializer
)


class LeitoViewSet(viewsets.ModelViewSet):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer


class InternacaoViewSet(viewsets.ModelViewSet):
    queryset = Internacao.objects.all()
    serializer_class = InternacaoSerializer


class RelatorioFinanceiroViewSet(viewsets.ModelViewSet):
    queryset = RelatorioFinanceiro.objects.all()
    serializer_class = RelatorioFinanceiroSerializer


class SuprimentoViewSet(viewsets.ModelViewSet):
    queryset = Suprimento.objects.all()
    serializer_class = SuprimentoSerializer