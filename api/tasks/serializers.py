from rest_framework import serializers

from api.users.serializers import UserSerializer, UserModel
from tasks.models import TaskModel


class TaskWriteSerializer(serializers.ModelSerializer):
    reporter = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    assignee = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())

    class Meta:
        model = TaskModel
        fields = "__all__"


class TaskReadSerializer(serializers.ModelSerializer):
    reporter = UserSerializer()
    assignee = UserSerializer()

    class Meta:
        model = TaskModel
        fields = "__all__"
