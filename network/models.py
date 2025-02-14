from django.db import models


class NetworkNode(models.Model):
    """Модель сетевого узла"""
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'ИП')
    ]
    name = models.CharField(max_length=255, verbose_name='Имя', unique=True)
    email = models.EmailField(verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name='clients', verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, default=0, decimal_places=2,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, editable=False, default=0,
                                             verbose_name='Уровень поставщика')

    def save(self, *args, **kwargs):
        if self.supplier:
            self.level = self.supplier.level + 1
        else:
            self.level = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сетевой узел'
        verbose_name_plural = 'Сетевые узлы'


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    network_node = models.ForeignKey(NetworkNode, related_name='products', on_delete=models.CASCADE,
                                     verbose_name='Сетевой узел')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
