from django.db import models

class Order(models.Model):
    boat = models.ForeignKey('boat.Boat', on_delete=models.CASCADE, verbose_name='лодка')

    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.CharField(max_length=150, verbose_name='электронная почта')
    message = models.TextField(verbose_name='сообщение')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    closed = models.BooleanField(default=False, verbose_name='заказ закрыт')

    def __str__(self):
        return f'Заказ {self.boat} - {self.email}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
