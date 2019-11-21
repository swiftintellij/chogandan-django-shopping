from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from rest_framework import mixins
from rest_framework import generics
from customer.models import Customer
from customer.serializers import CustomerSerializer
from .forms import JoinForm, LoginForm


def index(request):
    return render(request, "index.html", {'email': request.session.get("customer_email")})


class JoinView(FormView):
    template_name = "join.html"
    form_class = JoinForm
    success_url = "/"

    def form_valid(self, form):
        email = form.data.get("email")
        password = form.data.get("password")
        customer = Customer(email=email, password=make_password(password))
        customer.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        self.request.session["customer_email"] = form.email
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


def logout(request):
    if "customer_email" in request.session:
        del (request.session["customer_email"])
    return redirect("/login")


class CustomerListApiView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all().order_by("-id")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomerApiView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all().order_by("-id")

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
