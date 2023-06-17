from django.urls import path
from .views import sign_up_view, sing_in_view, logout_view


app_name = 'users'

urlpatterns = [
    path('sign-up/', sign_up_view, name='sign_up'),  # Сторінка реєстрації користувача
    path('sign-in/', sing_in_view, name='sing_in'),  # Сторінка входу користувача
    path('logout/', logout_view, name='logout'),  # Сторінка виходу користувача
]
