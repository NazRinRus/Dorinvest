from django.db import models
from exhibition.models import participant, partner


class Exhibition(models.Model):
    name = models.CharField("Название выставки", max_length=30, null=True)
    bunner = models.CharField("Изображение баннера", max_length=255, null=False)
    date_begin = models.DateTimeField("Дата начала выставки")
    date_end = models.DateTimeField("Дата окончания выставки")
    location = models.CharField("Место проведения", max_length=30, null=False)
    participants = models.ManyToManyField(
        participant.Participant, 'exhibition_participant', blank=True, through='ExhibitionParticipant'
    )
    partners = models.ManyToManyField(
        partner.Partner, 'exhibition_partner', blank=True
    )

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'
        ordering = ('date_begin', 'name',)

    def __str__(self):
        return f'{self.name} ({self.pk}) {self.date_begin}'

class Foto(models.Model):
    foto = models.CharField("Фотография", max_length=255, null=False)
    description = models.CharField("Описание фотографии", max_length=255, null=True)
    exhibition_id = models.ForeignKey(
        Exhibition, models.PROTECT, 'exhibition_foto', verbose_name='ID выставки'
    )

    class Meta:
        verbose_name = 'Фотография выставки'
        verbose_name_plural = 'Фотографии выставки'

    def __str__(self):
        return f'{self.description} ({self.pk})'

class ExhibitionParticipant(models.Model):
    exhibition_id = models.ForeignKey(
        Exhibition, models.PROTECT, 'exhibitions', verbose_name='ID выставки'
    )
    participant_id = models.ForeignKey(
        participant.Participant, models.PROTECT, 'participants', verbose_name='ID участника'
    )

    class Meta:
        verbose_name = 'Сводная таблица выставок и участников'
        verbose_name_plural = 'Сводные таблицы выставок и участников'
        ordering = ('-exhibition_id', 'participant_id',)

    def __str__(self):
        return f'({self.pk}) {self.exhibition_id__date_begin} {self.exhibition_id__name} {self.participant_id__name}'

class ExhibitionPartner(models.Model):
    exhibition_id = models.ForeignKey(
        Exhibition, models.PROTECT, 'exhibitions_partners', verbose_name='ID выставки'
    )
    partner_id = models.ForeignKey(
        partner.Partner, models.PROTECT, 'partners', verbose_name='ID партнера'
    )

    class Meta:
        verbose_name = 'Сводная таблица выставок и партнеров'
        verbose_name_plural = 'Сводные таблицы выставок и партнеров'
        ordering = ('-exhibition_id', 'partner_id',)

    def __str__(self):
        return f'({self.pk}) {self.exhibition_id__date_begin} {self.exhibition_id__name} {self.partner_id__name}'