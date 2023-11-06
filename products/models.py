from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение (превью)', upload_to='images/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_of_change = models.DateTimeField(auto_now=True, verbose_name='дата полследнего изменения')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
