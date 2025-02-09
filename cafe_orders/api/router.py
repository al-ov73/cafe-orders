from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView

router = DefaultRouter(trailing_slash=True)

urlpatterns = router.urls

urlpatterns.extend([
    path('api/orders/', OrderListCreateAPIView.as_view(), name='api_order_list_create'),
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='api_order_detail'),
])
