from django.urls import path
from .views import TaskListView, TaskDeleteView, AboutPageView, TaskCreateView, TaskDetailView, TaskUpdateView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='short_index'),
    path('tasks/', TaskListView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('create/', TaskCreateView.as_view(), name='create'),  # Сторінка створення завдання
    path('<uuid:uuid>/', TaskDetailView.as_view(), name='detail'),  # Перегляд деталей одного завдання.
    path('<uuid:uuid>/update/', TaskUpdateView.as_view(), name='update'),  # Сторінка зміни завдання
    path('<uuid:uuid>/delete/', TaskDeleteView.as_view(), name='delete'),  # Сторінка видалення завдання
]
