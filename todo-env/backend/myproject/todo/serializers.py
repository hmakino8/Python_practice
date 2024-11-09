from rest_framework import serializers
from .models import Todo

'''
  TodoモデルをJSON形式に変換するために使用。
  APIからのデータ取得やデータ登録・更新時に、
  このシリアライザーがDjangoとReact間のデータ交換を行う。
'''


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
