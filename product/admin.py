from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "display_price", "stock", "created_at", )
    search_fields = ["title", ]
    ordering = ("-id", )


admin.site.register(Product, ProductAdmin)
