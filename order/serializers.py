from rest_framework import serializers

from customer.serializers import CustomerSerializer
from order.models import Order
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "product", "quantity", "created_at"]