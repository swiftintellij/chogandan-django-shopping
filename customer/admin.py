from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "created_at", )
    search_fields = ["email", ]
    ordering = ("-id", )


admin.site.register(Customer, CustomerAdmin)