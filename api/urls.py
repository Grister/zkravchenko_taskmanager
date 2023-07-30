from django.urls import path, include
from rest_framework.authtoken import views


app_name = 'api'

urlpatterns = [
    path('tasks/', include('api.tasks.urls', namespace='tasks_api')),
    path('users/', include('api.users.urls', namespace='users_api')),
    path('auth/', views.obtain_auth_token)
]
