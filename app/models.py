from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField('Категория', max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True, default=None, blank=True
    )
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



