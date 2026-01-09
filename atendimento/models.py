from django.db import models
from django.conf import settings
from usuarios.models import Paciente


class Prontuario(models.Model):
    TIPO_CHOICES = (('presencial', 'Presencial'), ('tele', 'Telemedicina'))
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='historico')
    medico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_atendimento = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='presencial')

    queixa_principal = models.TextField()
    diagnostico = models.TextField()
    prescricao = models.TextField()
    evolucao_clinica = models.TextField()

    hash_seguranca = models.CharField(max_length=64, editable=False, null=True)

    def __str__(self):
        return f"Atendimento {self.paciente.nome} - {self.data_atendimento.strftime('%d/%m/%Y')}"