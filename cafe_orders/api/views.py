from rest_framework import generics

from .serializers import OrderSerializer
from ..orders.models import Order


# Список заказов + создание нового заказа
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Получение, обновление и удаление конкретного заказа
class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
