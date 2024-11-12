from django.contrib import admin
from django.urls import path

from blog.views import frontpage, post_detail

'''
  <slug:slug>
  左側のslugはdjangoのビルトインパターン
  右側のslugはpost_detail関数の引数

  localhost:8000/post-*
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage),
    path('<slug:slug>/', post_detail, name="post_detail")
]
