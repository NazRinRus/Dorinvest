from django.db import models
from exhibition.models import participant, partner


class Exhibition(models.Model):
    name = models.CharField("Название выставки", max_length=30, null=True)
    bunner = models.ImageField("Баннер")
    date = models.DateTimeField("Дата проведения")
    location = models.CharField("Место проведения", max_length=30, null=False)
    participants = models.ManyToManyField(
        participant.Participant, 'exhibition_participant', blank=True
    )
    foto_id = models.ForeignKey(
        'Foto', models.CASCADE, 'foto_exhibition', verbose_name='Фотографии'
    )
    partners = models.ManyToManyField(
        partner.Partner, 'exhibition_partner', blank=True
    )

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'
        ordering = ('date', 'name',)

    def __str__(self):
        return f'{self.name} ({self.pk}) {self.date}'

class Foto(models.Model):
    foto = models.CharField("Фотография", max_length=255, null=False)
    description = models.CharField("Описание фотографии", max_length=255, null=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.description} ({self.pk})'