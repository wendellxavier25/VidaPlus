from django.contrib import admin
from .models import Leito, Internacao, RelatorioFinanceiro, Suprimento, UnidadeSaude

admin.site.register(Leito)
admin.site.register(Internacao)
admin.site.register(RelatorioFinanceiro)
admin.site.register(Suprimento)
admin.site.register(UnidadeSaude)