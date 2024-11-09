from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'list', ListViewSet)
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
