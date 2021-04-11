from .views import USerViewSet , TasklistApi , DetailAPi
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('profile', USerViewSet)

urlpatterns = [
    path('<int:pk>/',DetailAPi.as_view(),name="detail_task"),
    path("",TasklistApi.as_view(),name="list_tasks"),
    path("", include(router.urls))
]
