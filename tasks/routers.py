from rest_framework import routers
from django.urls import path
# from .api import TaskViewSet
from .views import IndexView

router = routers.DefaultRouter()

# router.register("v1/tasks", TaskViewSet, "tasks")

urlpatterns = [
    path("tasks", IndexView.as_view(), name="index")
]

urlpatterns += router.urls
