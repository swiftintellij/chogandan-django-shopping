from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=265, verbose_name="상품명")
    display_price = models.IntegerField(verbose_name="가격")
    description = models.TextField(verbose_name="설명")
    stock = models.IntegerField(verbose_name="재고", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "product"
        verbose_name = "상품"
        verbose_name_plural = "상품"
