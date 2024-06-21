from django.db import models

class Article(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
        null=True,
        blank=True
    )
    content = models.TextField(
        verbose_name='Содержание',
        null=True,
        blank=True
    )
    is_draft = models.BooleanField(
        verbose_name='Черновик',
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалена',
        null=True,
        blank=True
    )
    published_date = models.DateTimeField(
        verbose_name='Дата',
        null=True,
        blank=True
    )
