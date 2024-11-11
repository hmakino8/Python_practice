from django.contrib import admin
from django.urls import path
from crud import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),  # pathが空の場合、ルートURLになる
    path('crud/', views.ProductListView.as_view(), name='list'),
    path('crud/new/', views.ProductCreateView.as_view(), name="new"),
    path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),
    path('crud/detail/<int:pk>', views.ProductDetailView.as_view(), name="detail"),
]

# 開発モードの場合のみ静的ファイルを直接表示できるようにする。
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
