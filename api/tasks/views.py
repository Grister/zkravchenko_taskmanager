from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.tasks.permissions import TaskPermission, CanChangeTask, CanDeleteTask
from api.tasks import serializers
from tasks.models import TaskModel


class TaskModelViewSet(ModelViewSet):
    queryset = TaskModel.objects.all()
    permission_classes = [IsAuthenticated, TaskPermission, CanChangeTask, CanDeleteTask]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.TaskReadSerializer
        return serializers.TaskWriteSerializer

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)
