from rest_framework import routers
from .views import PacienteViewSet, ConsultaViewSet, ExameViewSet

router = routers.DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'exames', ExameViewSet)

urlpatterns = router.urls
