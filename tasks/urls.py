from django.urls import path
from .views import index_view, about_view, create_view, detail_view, update_view, delete_view


app_name = 'tasks'

urlpatterns = [
    path('', index_view, name='short_index'),
    path('tasks/', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('create/', create_view, name='create'),  # Сторінка створення завдання
    path('<uuid:uuid>/', detail_view, name='detail'),  # Перегляд деталей одного завдання.
    path('<uuid:uuid>/update/', update_view, name='update'),  # Сторінка зміни завдання
    path('<uuid:uuid>/delete/', delete_view, name='delete'),  # Сторінка видалення завдання
]
