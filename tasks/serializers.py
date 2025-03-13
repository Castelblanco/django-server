from rest_framework import serializers, pagination
from .models import Task


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'created_at',
        )
        read_only_fields = ('created_at', )


class TaskPagination(pagination.LimitOffsetPagination):
    default_limit = 50
