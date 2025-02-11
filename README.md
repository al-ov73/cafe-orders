#### Приложение для управления заказами в кафе

Приложение, позволяющее Вам управлять заказами в вымышленном кафе.
<br/>
Доступен следующий функционал:
<br/><br/>
`/orders` - страница просмотра всех имеющихся заказов с выводом стола, общей стоимости заказа и его статуса
<br/><img src="https://github.com/user-attachments/assets/4775fb6c-5d9b-4119-bbb6-437612b670e0" alt="image" width="600" height="300"><br/>
<br/><br/>
`orders/create` - страница создания заказа
<br/><img src="https://github.com/user-attachments/assets/1673ba41-e6ec-4de5-95b1-21f9edb164e8" alt="image" width="200" height="200"><br/>
<br/><br/>
`orders/delete` - страница удаления заказа
<br/><img src="https://github.com/user-attachments/assets/ca3c3678-7294-4ce3-b1c9-3036c4156f8b" alt="image" width="300" height="200"><br/>
<br/><br/>
`orders/revenue` - страница подсчета выручки от оплаченных заказов
<br/><img src="https://github.com/user-attachments/assets/cbb92123-cdf6-4d6a-bcc7-904940a3a7ae" alt="image" width="400" height="200"><br/>
<br/><br/>
Примеры запросов к API
1. Получение списка всех заказов

`GET /api/orders/`

Ответ:

```
[
    {
        "id": 1,
        "table_number": 5,
        "items": [
            {
                "id": 1,
                "name": "Кофе",
                "price": "5.00",
                "description": "Ароматный кофе",
                "created_at": "2023-10-01T12:00:00Z",
                "updated_at": "2023-10-01T12:00:00Z"
            },
            {
                "id": 2,
                "name": "Пирог",
                "price": "10.00",
                "description": "Яблочный пирог",
                "created_at": "2023-10-01T12:00:00Z",
                "updated_at": "2023-10-01T12:00:00Z"
            }
        ],
        "total_price": "15.00",
        "status": "pending",
        "created_at": "2023-10-01T12:00:00Z",
        "updated_at": "2023-10-01T12:00:00Z"
    }
]
```
2. Создание нового заказа

`POST /api/orders/`
Тело запроса:

```
{
    "table_number": 3,
    "items": [1, 2],
    "status": "pending"
}
```
Ответ:

```
{
    "id": 2,
    "table_number": 3,
    "items": [
        {
            "id": 1,
            "name": "Кофе",
            "price": "5.00",
            "description": "Ароматный кофе",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z"
        },
        {
            "id": 2,
            "name": "Пирог",
            "price": "10.00",
            "description": "Яблочный пирог",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z"
        }
    ],
    "total_price": "15.00",
    "status": "pending",
    "created_at": "2023-10-01T12:00:00Z",
    "updated_at": "2023-10-01T12:00:00Z"
}
```

3. Получение информации о конкретном заказе

Запрос:

`GET /api/orders/1/`

Ответ:

```
{
    "id": 1,
    "table_number": 5,
    "items": [
        {
            "id": 1,
            "name": "Кофе",
            "price": "5.00",
            "description": "Ароматный кофе",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z"
        },
        {
            "id": 2,
            "name": "Пирог",
            "price": "10.00",
            "description": "Яблочный пирог",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z"
        }
    ],
    "total_price": "15.00",
    "status": "pending",
    "created_at": "2023-10-01T12:00:00Z",
    "updated_at": "2023-10-01T12:00:00Z"
}
```

4. Обновление заказа

Запрос:

`PUT /api/orders/1/`

Тело запроса:

```
{
    "table_number": 5,
    "items": [1, 2, 3],
    "status": "ready"
}
```
Ответ:

```
{
    "id": 1,
    "table_number": 5,
    "items": [
        {
            "id": 1,
            "name": "Кофе",
            "price": "5.00",
            "description": "Ароматный кофе",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z"
        },
        {
            "id": 2,
            "name": "Пирог",
            "price": "10.00",
            "description": "Яблочный пирог",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z"
        },
        {
            "id": 3,
            "name": "Чай",
            "price": "3.00",
            "description": "Зеленый чай",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z"
        }
    ],
    "total_price": "18.00",
    "status": "ready",
    "created_at": "2023-10-01T12:00:00Z",
    "updated_at": "2023-10-01T12:05:00Z"
}
```

5. Удаление заказа

Запрос:

`DELETE /api/orders/1/`

Ответ:

```
{
    "detail": "Заказ успешно удален."
}
```

---

#### Развернуть локально через Poetry:

1. Установить Poetry, если еще не установлен

```
curl -sSL https://install.python-poetry.org | python3 -
```
2. Клонировать себе проект

```
git clone git@github.com:al-ov73/cafe-orders.git
```

3. Развернуть локально СУБД Postgres и создать в ней базу данных
```
CREATE DATABASE cafe_orders;
```

4. Установить зависимости
```
poetry install
```

5. Запустить проект (автоматически применятся миграции)
```
make start
```

---

#### Запустить тесты:

```
make test
```
