from django.contrib import admin
from .models import USerProfile, task
from django.contrib.auth.models import Group

# Register your models here.


admin.site.register(USerProfile)
admin.site.register(task)
