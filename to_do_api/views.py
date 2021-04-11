from django.shortcuts import render
from rest_framework import viewsets
from serializer import UserSerializer
from .models import USerProfile


class USerViewSet(viewsets.ModelViewSet):
    """
    doing CRUD operation using viewset
    """
    serializer_class = UserSerializer
    queryset = USerProfile.objects.all()
