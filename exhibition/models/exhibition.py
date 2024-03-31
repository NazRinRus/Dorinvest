from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Exhibition(models.Model):
    name = models.CharField("Название выставки", max_length=30, null=True)
    bunner = models.ImageField("Баннер")
    date = models.DateTimeField("Дата проведения")
    location = models.CharField("Место проведения", max_length=30, null=False)

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'
        ordering = ('date', 'name',)

    def __str__(self):
        return f'{self.name} ({self.pk}) {self.date}'