from django.contrib import admin
from .models import Order, Item

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('table_number', 'status')

admin.site.register(Item)
