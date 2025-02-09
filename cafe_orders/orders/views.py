from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

def order_list(request):
    """Отображение списка заказов с возможностью поиска"""
    query = request.GET.get('q')
    if query:
        orders = Order.objects.filter(table_number__icontains=query) | Order.objects.filter(status__icontains=query)
    else:
        orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders, 'query': query})


def order_create(request):
    """Создание нового заказа"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def order_update(request, order_id):
    """Обновление заказа (изменение статуса)"""
    order = get_object_or_404(Order, id=order_id)
    print(order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

def order_delete(request, order_id):
    """Удаление заказа"""
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})

def revenue_report(request):
    """Расчет общей выручки за оплаченные заказы"""
    revenue = Order.objects.filter(status='paid').aggregate(total=models.Sum('total_price'))['total'] or 0
    return render(request, 'orders/revenue_report.html', {'revenue': revenue})