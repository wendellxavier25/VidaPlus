from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import UnidadeSaude, Leito, Internacao, RelatorioFinanceiro, Suprimento
from .serializers import UnidadeSaudeSerializer, LeitoSerializer, InternacaoSerializer, RelatorioFinanceiroSerializer, SuprimentoSerializer


class UnidadeSaudeViewSet(viewsets.ModelViewSet):
    queryset = UnidadeSaude.objects.all()
    serializer_class = UnidadeSaudeSerializer
    permission_classes = [IsAdminUser]

class SuprimentoViewSet(viewsets.ModelViewSet):
    queryset = Suprimento.objects.all()
    serializer_class = SuprimentoSerializer
    permission_classes = [IsAdminUser]

class LeitoViewSet(viewsets.ModelViewSet):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    

class InternacaoViewSet(viewsets.ModelViewSet):
    queryset = Internacao.objects.all().order_by('-data_entrada')
    serializer_class = InternacaoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.data_saida and instance.leito.status == 'ocupado':
            instance.leito.status = 'livre'
            instance.leito.save()


class RelatorioFinanceiroViewSet(viewsets.ModelViewSet):
    queryset = RelatorioFinanceiro.objects.all().order_by('-data')
    serializer_class = RelatorioFinanceiroSerializer
    permission_classes = [IsAdminUser]