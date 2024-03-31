from django.db import models


class Partner(models.Model):
    name = models.CharField("Имя партнера", max_length=30, null=False)
    logo = models.CharField("Логотип", max_length=30, null=True)
    info = models.TextField("Описание партнера", null=True)
    website = models.CharField("Ссылка на вебресурс", max_length=255, null=True)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'
