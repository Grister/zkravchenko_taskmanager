from django.urls import path

from api.users import views

app_name = 'users_api'

urlpatterns = [
    path("", views.UserListAPIView.as_view(), name="user-list"),
    path("<int:pk>/", views.UserDetailAPIView.as_view(), name="user-detail"),
]
