from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CounterViewSet

router = DefaultRouter()
router.register(r'counters', CounterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
