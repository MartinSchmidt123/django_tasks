from rest_framework.routers import DefaultRouter

from tasks.views import BadTaskViewSet, GoodTaskViewSet

router = DefaultRouter()

router.register(r'good', GoodTaskViewSet, basename='tasks-good')
router.register(r'bad', BadTaskViewSet, basename='tasks-bad')

urlpatterns = router.urls
