from .models import USerProfile, task
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USerProfile
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}
                         }}

    def create_user_serializer(self, data):
        """serialize new user """
        user = USerProfile(
            email=data['email'],
            password=data['password']

        )

        return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ['id', 'body']
