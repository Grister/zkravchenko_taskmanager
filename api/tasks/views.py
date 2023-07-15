from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.tasks.serializers import TaskSerializer
from tasks.models import TaskModel


class TaskListAPIView(ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
