from .models import Task
from rest_framework import viewsets, permissions, filters
from .serializers import TaskSerializers, TaskPagination
from django_filters.rest_framework import DjangoFilterBackend
from .tasks import send_task_confimation_email


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializers
    pagination_class = TaskPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', ]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer: TaskSerializers):
        task = serializer.save()
        send_task_confimation_email.delay(task.id, "ejcastelg@gmail.com")
