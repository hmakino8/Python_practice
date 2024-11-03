from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)  # 商品名を文字列で定義　最大文字列長は200
    price = models.PositiveIntegerField()  # 価格を整数で定義　正の整数のみ

    def __str__(self):
        return self.name
