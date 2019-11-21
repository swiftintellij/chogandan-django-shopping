from django.contrib import admin
from django.urls import path
from customer.views import index, JoinView, LoginView, logout, CustomerListApiView, CustomerApiView
from order.views import OrderAddView, OrderListView, OrderListApiView, OrderApiView
from product.views import ProductListView, ProductAddView, ProductView, ProductListApiView, ProductApiView

urlpatterns = [
    path("s/a/console/", admin.site.urls),
    path('', index),
    path("join/", JoinView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", logout),
    path("product/", ProductListView.as_view()),
    path("product/add", ProductAddView.as_view()),
    path("product/<int:pk>", ProductView.as_view()),
    path("order/", OrderListView.as_view()),
    path("order/add", OrderAddView.as_view()),
    path("api/product", ProductListApiView.as_view()),
    path("api/product/<int:pk>", ProductApiView.as_view()),
    path("api/customer", CustomerListApiView.as_view()),
    path("api/customer/<int:pk>", CustomerApiView.as_view()),
    path("api/order", OrderListApiView.as_view()),
    path("api/order/<int:pk>", OrderApiView.as_view()),
]
