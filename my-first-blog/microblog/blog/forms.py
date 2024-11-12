from django import forms
from .models import Comment


'''
  Metaクラスはmodelの設定を行う
  metaとは、一般的に〜についてのという意味をもち、ある対象を超えて、
  その対象自体についての情報や概念を指す際に使われる。
'''


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
