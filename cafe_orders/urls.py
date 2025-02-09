from django.contrib import admin
from django.urls import path,  include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('orders/', include('cafe_orders.orders.urls')),
    path('api/', include('cafe_orders.api.router')),
]
