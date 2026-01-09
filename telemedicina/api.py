from rest_framework import routers
from .views import TeleConsultaViewSet, ProntuarioViewSet

router = routers.DefaultRouter()
router.register(r"teleconsultas", TeleConsultaViewSet)
router.register(r"prontuarios", ProntuarioViewSet)

urlpatterns = router.urls