from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    PERFIS = (
        ("paciente", "Paciente"),
        ("medico", "Médico"),
        ("admin", "Administrador"),
    )
    perfil = models.CharField(max_length=20, choices=PERFIS, default="paciente")
    

class Paciente(models.Model):
    usuario = models.OneToOneField(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='perfil_paciente', 
        null=True, 
        blank=True
    )
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    consentimento_lgpd = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.nome} - {self.cpf}"


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    profissional = models.ForeignKey('profissionais.Profissional', on_delete=models.SET_NULL, null=True, related_name='consultas')
    data_consulta = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('agendado','Agendado'),('cancelado','Cancelado'),('finalizado','Finalizado')], default='agendado')
    tipo = models.CharField(max_length=20, choices=[('presencial','Presencial'),('telemedicina','Telemedicina')], default='presencial')
    criado_em = models.DateTimeField(auto_now_add=True)


class Exame(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='exames')
    descricao = models.TextField()
    data = models.DateField()
    resultado = models.TextField(null=True, blank=True)
    arquivos = models.JSONField(default=list, blank=True)