from django.db import models
from django.conf import settings
from django.utils import timezone

class UnidadeSaude(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.nome


class Leito(models.Model):
    unidade = models.ForeignKey(UnidadeSaude, on_delete=models.CASCADE, related_name="leitos", null=True)
    numero = models.CharField(max_length=10)
    status = models.CharField(
        max_length=20,
        choices=[("livre", "Livre"), ("ocupado", "Ocupado")],
        default="livre"
    )

    def __str__(self):
        return f"{self.unidade.nome} - Leito {self.numero} ({self.status})"



class Internacao(models.Model):
    paciente = models.ForeignKey('usuarios.Paciente', on_delete=models.CASCADE, related_name="internacoes")
    leito = models.ForeignKey(Leito, on_delete=models.CASCADE)
    data_entrada = models.DateTimeField(default=timezone.now)
    data_saida = models.DateTimeField(null=True, blank=True)
    registrado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.paciente.nome} - Leito {self.leito.numero}"


class RelatorioFinanceiro(models.Model):
    tipo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.tipo} - R$ {self.valor}"


class Suprimento(models.Model):
    paciente = models.ForeignKey(
        'usuarios.Paciente',
        on_delete=models.CASCADE,
        related_name='suprimentos'
    )

    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    registrado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nome} - {self.quantidade} unidades"
