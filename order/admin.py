from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "product", "created_at",)
    search_fields = ["product", ]
    ordering = ("-id", )


admin.site.register(Order, OrderAdmin)
