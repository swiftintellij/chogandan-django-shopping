from django.db import transaction
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import FormView

from customer.decorators import login_required
from customer.models import Customer
from order.forms import OrderForm
from order.models import Order
from order.serializers import OrderSerializer
from product.models import Product
from rest_framework import mixins
from rest_framework import generics

class OrderAddView(FormView):
    form_class = OrderForm
    success_url = "/product/"

    def form_valid(self, form):
        quantity = form.data.get("quantity")
        product_id = form.data.get("product_id")
        email = self.request.session.get("customer_email")
        product = Product.objects.get(pk=product_id)

        with transaction.atomic():
            order = Order(
                quantity=quantity,
                product=Product.objects.get(pk=product_id),
                customer=Customer.objects.get(email=email),
            )
            product.stock -= int(quantity)
            order.save()
            product.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect("/product/" + str(form.product_id))

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs


@method_decorator(login_required, name="dispatch")
class OrderListView(ListView):
    template_name = "order_list.html"
    context_object_name = "order_list"

    def get_queryset(self):
        return Order.objects.filter(customer__email=self.request.session.get("customer_email"))


class OrderListApiView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by("-id")[:1]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderApiView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by("id")

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)