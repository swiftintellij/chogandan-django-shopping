from django.db import models


class Customer(models.Model):
    email = models.EmailField(unique=True, verbose_name="이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="가입일")

    def __str__(self):
        return self.email

    class Meta:
        db_table = "customer"
        verbose_name = "고객"
        verbose_name_plural = "고객"
