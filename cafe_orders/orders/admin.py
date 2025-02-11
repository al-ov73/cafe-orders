from django.contrib import admin
from .models import Order, Item


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "get_items", "table_number", "total_price", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("table_number", "status")

    def get_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])

    get_items.short_description = "Блюда"


admin.site.register(Item)
