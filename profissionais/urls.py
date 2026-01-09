from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profissionais.api import ProfissionalViewSet, AgendaViewSet, PrescricaoViewSet

router = DefaultRouter()
router.register("profissionais", ProfissionalViewSet)
router.register("agendas", AgendaViewSet)
router.register("prescricoes", PrescricaoViewSet)

urlpatterns = [
    path("api/profissionais/", include(router.urls)),
]
