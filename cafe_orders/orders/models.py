from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.PositiveIntegerField(verbose_name="Номер стола")
    items = models.ManyToManyField(Item, verbose_name="Список блюд")
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name="Общая стоимость",
        editable=False, default=0
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def save(self, *args, **kwargs):
        """Рассчитываем сумму перед первым сохранением"""
        if not self.pk:  # Если объект создается впервые
            super().save(*args, **kwargs)  # Сначала сохраняем, чтобы получить ID

        self.total_price = sum(item.price for item in self.items.all())  # Вычисляем сумму
        super().save(update_fields=['total_price'])  # Обновляем только поле total_price

    def __str__(self):
        return f"Заказ {self.id} (Стол {self.table_number}) - {self.get_status_display()}"