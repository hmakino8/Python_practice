from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe


'''
  mark_safe: セキュリティ上の理由で、HTMLをエスケープするための関数
  デフォルトでは、HTMLタグはエスケープされるため、画像を表示できない。
  そのため、mark_safeを使ってエスケープを回避する。

  format: 文字列をフォーマットするための関数
  フォーマットした文字列を返す。
  {}を使って、変数を埋め込む。
'''


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image', 'description')
    search_fields = ('name',)
    list_filter = ('category',)

    def image(self, obj):
        return mark_safe('<img src="{}" style="width:100px height: auto;">'.format(obj.img.url))


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
