from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('tasks/', include('api.tasks.urls', namespace='tasks_api')),
    path('users/', include('api.users.urls', namespace='users_api')),
]
