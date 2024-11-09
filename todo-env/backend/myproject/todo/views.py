from rest_framework import viewsets
from .models import List, Task
from .serializers import ListSerializer, TaskSerializer

'''
  List, Taskモデルのデータを管理するためのViewSet。
  ModelViewSetを継承して、List, Taskモデルの全ての操作を行う。
'''


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
