from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.db.models.query import QuerySet
from .models import Order
from .forms import OrderForm


def order_list(request: HttpRequest) -> HttpResponse:
    """Отображение списка заказов с возможностью поиска"""
    query: str | None = request.GET.get("q")
    orders: QuerySet[Order]

    if query:
        orders = Order.objects.filter(table_number__icontains=query) | Order.objects.filter(
            status__icontains=query
        ).order_by("id")
    else:
        orders = Order.objects.all().order_by("id")

    return render(request, "orders/order_list.html", {"orders": orders, "query": query})


def order_create(request: HttpRequest) -> HttpResponse:
    """Создание нового заказа"""
    if request.method == "POST":
        form: OrderForm = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_list")
    else:
        form = OrderForm()

    return render(request, "orders/order_form.html", {"form": form})


def order_update(request: HttpRequest, order_id: int) -> HttpResponse:
    """Обновление заказа (изменение статуса)"""
    order: Order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        form: OrderForm = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_list")
    else:
        form = OrderForm(instance=order)

    return render(request, "orders/order_form.html", {"form": form})


def order_delete(request: HttpRequest, order_id: int) -> HttpResponse:
    """Удаление заказа"""
    order: Order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        order.delete()
        return redirect("order_list")

    return render(request, "orders/order_confirm_delete.html", {"order": order})


def revenue_report(request: HttpRequest) -> HttpResponse:
    """Расчет общей выручки за оплаченные заказы"""
    revenue: float = Order.objects.filter(status="paid").aggregate(total=Sum("total_price"))["total"] or 0
    return render(request, "orders/revenue_report.html", {"revenue": revenue})
