from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product  # .modelsとすることで、同じディレクトリにあるmodels.pyを参照
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm


class TopView(TemplateView):
    template_name = "top.html"  # テンプレートファイルの指定


"""
ListViewは、template_nameを指定しない場合、
モデル名_list.htmlというテンプレートファイルを参照する
"""


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "list.html"
    paginate_by = 3


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'


'''
UpdateViewは、指定されたプライマリキーに基づいて
データベースからオブジェクトを取得し、フォームにそのオブジェクトのデータを埋め込む。
'''


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('list')


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'
