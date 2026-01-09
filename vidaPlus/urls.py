from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


from hospital.api import LeitoViewSet, InternacaoViewSet, RelatorioFinanceiroViewSet, SuprimentoViewSet
from usuarios.api import PacienteViewSet, ConsultaViewSet, ExameViewSet
from profissionais.api import ProfissionalViewSet, AgendaViewSet, PrescricaoViewSet

router = DefaultRouter()

router.register(r"leitos", LeitoViewSet)
router.register(r"internacoes", InternacaoViewSet)
router.register(r"financeiro", RelatorioFinanceiroViewSet)
router.register(r"suprimentos", SuprimentoViewSet)

router.register(r"pacientes", PacienteViewSet)
router.register(r"consultas", ConsultaViewSet)
router.register(r"exames", ExameViewSet)

router.register(r"profissionais", ProfissionalViewSet)
router.register(r"agenda", AgendaViewSet)
router.register(r"prescricoes", PrescricaoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/", include(router.urls)),
    path("api/telemedicina/", include("telemedicina.api")),
    path("api/usuarios/", include("usuarios.api")),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]