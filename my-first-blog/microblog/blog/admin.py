from django.contrib import admin
from .models import Post, Comment

'''
  管理サイトにPostモデルを登録する
'''
admin.site.register(Post)
admin.site.register(Comment)
