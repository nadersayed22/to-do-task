from .views import USerViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('profile', USerViewSet)

urlpatterns = [

    path("", include(router.urls))
]
