# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class News(models.Model):
    title = models.CharField('Заголовок',max_length=50)
    short_description = models.CharField('Краткое описание',max_length=200)
    content = models.TextField('Текст', max_length=2000)
    published_date = models.DateTimeField('Дата публикации',default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'