from django.urls import path
from rest_framework.routers import SimpleRouter

from api.tasks import views

app_name = 'tasks_api'

router = SimpleRouter()
router.register('', views.TaskModelViewSet, 'task')

urlpatterns = router.urls
