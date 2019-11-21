from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from django.views import View

from order.forms import OrderForm
from product.forms import ProductForm
from product.models import Product
from rest_framework import generics
from rest_framework import mixins

from product.serializers import ProductSerializer


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.order_by('-id')


class ProductAddView(FormView):
    model = Product
    template_name = "product_add.html"
    form_class = ProductForm
    success_url = "/product/"

    def form_valid(self, form):
        title = form.data.get("title")
        display_price = form.data.get("display_price")
        description = form.data.get("description")
        stock = form.data.get("stock")

        product = Product(
            title=title,
            display_price=display_price,
            description=description,
            stock=stock
        )
        product.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProductView(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = "product"
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = OrderForm(self.request)
        return context


class ProductListApiView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("-id")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductApiView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("-id")

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

