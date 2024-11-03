from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product  # .modelsとすることで、同じディレクトリにあるmodels.pyを参照


class TopView(TemplateView):
    template_name = "top.html"  # テンプレートファイルの指定


"""
ListViewは、template_nameを指定しない場合、
モデル名_list.htmlというテンプレートファイルを参照する
"""


class ProductListView(ListView):
    model = Product
    template_name = "list.html"
    paginate_by = 3
