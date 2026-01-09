from django.db import models
from usuarios.models import Paciente, Consulta
from profissionais.models import Profissional



class TeleConsulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="teleconsultas")
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name="teleconsultas")
    data = models.DateTimeField()
    link = models.URLField()
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"TeleConsulta - {self.paciente.nome} com {self.profissional.nome}"
    
class Prontuario(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE, related_name="prontuario")
    diagnostico = models.TextField()
    observacoes = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Prontuário da consulta {self.consulta.id}"