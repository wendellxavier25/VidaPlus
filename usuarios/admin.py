from django.contrib import admin
from .models import Paciente, Exame, Consulta, Usuario

admin.site.register(Usuario)

admin.site.register(Paciente)

admin.site.register(Exame)

admin.site.register(Consulta)