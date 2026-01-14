from django.db import models
from django.conf import settings

class Profissional(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                   related_name='perfil_profissional', null=True)
    nome = models.CharField(max_length=200)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=[
        ("médico", "Médico"),
        ("enfermeiro", "Enfermeiro"),
        ("tecnico", "Tecnico")
    ])

    def __str__(self):
        return f"{self.nome} - {self.crm}"
    
class Agenda(models.Model):
    profissonal =  models.ForeignKey(Profissional, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    disponivel = models.BooleanField(default=True)

class Prescricao(models.Model):
    consulta = models.ForeignKey("usuarios.Consulta", on_delete=models.CASCADE)
    profissonal = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    texto = models.TextField()
    assinatura_digital = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True) 