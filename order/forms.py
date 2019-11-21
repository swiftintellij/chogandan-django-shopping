from django import forms
from django.db import transaction
from customer.models import Customer
from order.models import Order
from product.models import Product


class OrderForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            "required": "주문 수량을 입력하세요."
        },
        label="수량",
    )
    product_id = forms.IntegerField(
        error_messages={
            "required": "상품 번호가 없습니다."
        },
        label="상품",
        widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantity")
        product_id = cleaned_data.get("product_id")
        email = self.request.session.get("customer_email")
        product = Product.objects.get(pk=product_id)

        if not (email and product_id and product and 0 < quantity <= product.stock):
            self.product_id = product_id
            self.add_error("quantity", "수량을 확인하세요")
