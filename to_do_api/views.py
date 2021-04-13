from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializer import UserSerializer, TaskSerializer
from .models import UserProfile, Task


class UserViewSet(viewsets.ModelViewSet):
    """
    doing CRUD operation using viewset
    """
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()


class TaskListCreateAPIView(generics.ListCreateAPIView):
    """
    doing list & Create using post & get  method
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by('-modified_at')


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """doing delete & update & put  & get detail """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
