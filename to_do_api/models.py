from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django_timestamps.softDeletion import SoftDeletionModel
from django_timestamps.timestamps import TimestampsModel


# Create your models here.
class UserProfileManager(BaseUserManager):
    """"
    class required by django for managing our users from management command
    """

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users Must Have EMail Address")

        # create anew user object
        user = self.model(
            email=self.normalize_email(email),
        )
        # create new pass
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """"
        create and save new superuser with given details
        """

        # override on create fun
        user = self.create_user(email, password)

        # make this user an admin
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class USerProfile(AbstractBaseUser, PermissionsMixin):
    """
    a user profile in our system
    """
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        """
        What to show when we output an object as a string
        """

        return self.email


class task(models.Model):
    """
    model to create single task
    """
    body = models.TextField(max_length=255, null=True, blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """
        What to show when we output an object as a string
        """
        return self.body
