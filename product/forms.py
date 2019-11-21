from django import forms
from product.models import Product


class ProductForm(forms.Form):
    title = forms.CharField(
        error_messages={
            "required": "상품명을 입력하세요."
        },
        max_length=128,
        label="상품명",
    )
    display_price = forms.IntegerField(
        error_messages={
            "required": "가격을 입력하세요."
        },
        label="가격",
    )
    description = forms.CharField(
        error_messages={
            "required": "설명을 입력하세요"
        },
        label="설명"
    )
    stock = forms.IntegerField(
        error_messages={
            "required": "수량을 입력하세요."
        },
        label="수량"
    )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        display_price = cleaned_data.get("display_price")
        description = cleaned_data.get("description")
        stock = cleaned_data.get("stock")

        if not (title and display_price and description and stock):
            self.add_error("title", "상품등록이 실패했어요.")