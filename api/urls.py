from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet, SensorViewSet, EventoViewSet, BarreraViewSet

router = DefaultRouter()
router.register(r"departamentos", DepartamentoViewSet)
router.register(r"sensores", SensorViewSet)
router.register(r"eventos", EventoViewSet)
router.register(r"barreras", BarreraViewSet)

urlpatterns = router.urls
