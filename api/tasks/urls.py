from django.urls import path
from api.tasks import views

app_name = 'tasks_api'

urlpatterns = [
    path('', views.TaskListAPIView.as_view()),
    path('<uuid:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view())
]
