from .views import UserViewSet, TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('profile', UserViewSet)

urlpatterns = [
    path('todos/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name="detail_task"),
    path("todos/", TaskListCreateAPIView.as_view(), name="list_tasks"),
    path("", include(router.urls))
]
