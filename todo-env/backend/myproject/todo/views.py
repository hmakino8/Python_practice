from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

'''
  Todoモデルのデータを管理するためのViewSet。
  ModelViewSetを継承して、Todoモデルの全ての操作を行う。
'''


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
