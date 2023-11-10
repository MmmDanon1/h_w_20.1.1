from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    preview = models.ImageField(verbose_name='изображение (превью)', upload_to='images/', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    is_publish = models.BooleanField(default=True, verbose_name='публикации', **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
