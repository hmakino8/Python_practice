from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Description(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


'''
  on_delete=models.***

  紐づいているデータが削除された時の振る舞い

  CASCADE: 紐づいているデータが削除された時に、そのデータも削除される
  PROTECT: 紐づいているデータが削除された時に、エラーを返す
  SET_NULL: 紐づいているデータが削除された時に、NULLをセットする
  SET_DEFAULT: 紐づいているデータが削除された時に、デフォルト値をセットする
  SET(): 紐づいているデータが削除された時に、指定したデータをセットする
'''


class Product(models.Model):
    name = models.CharField(max_length=200)  # 商品名を文字列で定義　最大文字列長は200
    price = models.PositiveIntegerField()  # 価格を整数で定義　正の整数のみ
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, default='noImage.png')  # 画像フィールドは省略可で、デフォルト画像はnoImage.png
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list')
