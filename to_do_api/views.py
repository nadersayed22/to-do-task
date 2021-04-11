from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializer import UserSerializer, TaskSerializer
from .models import USerProfile, task


class USerViewSet(viewsets.ModelViewSet):
    """
    doing CRUD operation using viewset
    """
    serializer_class = UserSerializer
    queryset = USerProfile.objects.all()


class TasklistApi(generics.ListCreateAPIView):
    """
    doing list & Create using post & get  method
    """
    serializer_class = TaskSerializer
    queryset = task.objects.all()


class DetailAPi(generics.RetrieveUpdateDestroyAPIView):
    """doing delete & update & put """
    serializer_class = TaskSerializer
    queryset = task.objects.all()
