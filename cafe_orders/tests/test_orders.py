import pytest
from django.http import HttpRequest, HttpResponse
from django.test import RequestFactory
from unittest.mock import patch, MagicMock
from django.db.models import Sum
from cafe_orders.orders.views import (
    order_list,
    order_create,
    order_update,
    order_delete,
    revenue_report,
)
from cafe_orders.orders.models import Order
from cafe_orders.orders.forms import OrderForm


@pytest.fixture
def request_factory() -> RequestFactory:
    """Фабрика запросов для тестирования представлений Django."""
    return RequestFactory()


@pytest.fixture
def mock_order() -> MagicMock:
    """Создает мок-объект заказа для тестов."""
    order = MagicMock(spec=Order)
    order.id = 1
    order.table_number = 5
    order.status = "pending"
    order.total_price = 100.00
    return order


@pytest.fixture
def mock_order_queryset(mock_order: MagicMock) -> MagicMock:
    """Создает мок-объект QuerySet заказов."""
    return MagicMock(spec=Order.objects.all(), model=Order)


@patch("cafe_orders.orders.views.Order.objects")
def test_order_list(
    mock_order_objects: MagicMock, request_factory: RequestFactory, mock_order_queryset: MagicMock
) -> None:
    """Тестирует получение списка заказов."""
    mock_order_objects.all.return_value = mock_order_queryset
    mock_order_queryset.order_by.return_value = mock_order_queryset

    request: HttpRequest = request_factory.get("/orders/")
    response: HttpResponse = order_list(request)

    assert response.status_code == 200
    mock_order_objects.all.assert_called()


@patch("cafe_orders.orders.views.OrderForm")
def test_order_create_get(mock_form: MagicMock, request_factory: RequestFactory) -> None:
    """Тестирует отображение формы создания заказа (GET-запрос)."""
    mock_form.return_value = MagicMock()

    request: HttpRequest = request_factory.get("/orders/create/")
    response: HttpResponse = order_create(request)

    assert response.status_code == 200
    mock_form.assert_called_once()


@patch("cafe_orders.orders.views.OrderForm")
def test_order_create_post_valid(mock_form: MagicMock, request_factory: RequestFactory) -> None:
    """Тестирует успешное создание заказа (POST-запрос с валидными данными)."""
    mock_form.return_value = MagicMock(is_valid=MagicMock(return_value=True))

    request: HttpRequest = request_factory.post("/orders/create/", {})
    response: HttpResponse = order_create(request)

    assert response.status_code == 302
    mock_form.return_value.save.assert_called_once()


@patch("cafe_orders.orders.views.get_object_or_404")
@patch("cafe_orders.orders.views.OrderForm")
def test_order_update_get(
    mock_form: MagicMock, mock_get_object: MagicMock, request_factory: RequestFactory, mock_order: MagicMock
) -> None:
    """Тестирует отображение формы обновления заказа (GET-запрос)."""
    mock_get_object.return_value = mock_order
    mock_form.return_value = MagicMock()

    request: HttpRequest = request_factory.get(f"/orders/update/{mock_order.id}/")
    response: HttpResponse = order_update(request, mock_order.id)

    assert response.status_code == 200
    mock_get_object.assert_called_once_with(Order, id=mock_order.id)
    mock_form.assert_called_once_with(instance=mock_order)


@patch("cafe_orders.orders.views.get_object_or_404")
@patch("cafe_orders.orders.views.OrderForm")
def test_order_update_post_valid(
    mock_form: MagicMock, mock_get_object: MagicMock, request_factory: RequestFactory, mock_order: MagicMock
) -> None:
    """Тестирует успешное обновление заказа (POST-запрос с валидными данными)."""
    mock_get_object.return_value = mock_order
    mock_form.return_value = MagicMock(is_valid=MagicMock(return_value=True))

    request: HttpRequest = request_factory.post(f"/orders/update/{mock_order.id}/", {})
    response: HttpResponse = order_update(request, mock_order.id)

    assert response.status_code == 302
    mock_form.return_value.save.assert_called_once()


@patch("cafe_orders.orders.views.get_object_or_404")
def test_order_delete_post(mock_get_object: MagicMock, request_factory: RequestFactory, mock_order: MagicMock) -> None:
    """Тестирует успешное удаление заказа (POST-запрос)."""
    mock_get_object.return_value = mock_order

    request: HttpRequest = request_factory.post(f"/orders/delete/{mock_order.id}/")
    response: HttpResponse = order_delete(request, mock_order.id)

    assert response.status_code == 302
    mock_get_object.assert_called_once_with(Order, id=mock_order.id)
    mock_order.delete.assert_called_once()


@patch("cafe_orders.orders.views.Order.objects.filter")
@patch("cafe_orders.orders.views.Order.objects.aggregate")
def test_revenue_report(mock_aggregate: MagicMock, mock_filter: MagicMock, request_factory: RequestFactory) -> None:
    """Тестирует расчет общей выручки за оплаченные заказы."""
    mock_filter.return_value = MagicMock()
    mock_aggregate.return_value = {"total": 1000.00}

    request: HttpRequest = request_factory.get("/orders/revenue/")
    response: HttpResponse = revenue_report(request)

    assert response.status_code == 200
    mock_filter.assert_called_once_with(status="paid")
