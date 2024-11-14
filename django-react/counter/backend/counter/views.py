from rest_framework import viewsets
from .models import Counter
from .serializers import CounterSerializer


class CounterViewSet(viewsets.ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
