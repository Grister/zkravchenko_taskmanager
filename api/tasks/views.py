from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import SAFE_METHODS
from api.tasks import serializers
from tasks.models import TaskModel


class TaskListAPIView(ListCreateAPIView):
    queryset = TaskModel.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.TaskReadSerializer
        return serializers.TaskWriteSerializer


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.TaskReadSerializer
        return serializers.TaskWriteSerializer
