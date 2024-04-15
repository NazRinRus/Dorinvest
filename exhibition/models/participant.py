from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TypeParticipant(models.Model):
    code = models.CharField('Код', max_length=3, primary_key=True)
    name = models.CharField("Вид животного", max_length=30, null=False)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField("Активность", default=True)

    class Meta:
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Виды животных'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.code})'

class BreedParticipant(models.Model):
    code = models.CharField('Код', max_length=3, primary_key=True)
    name = models.CharField("Порода", max_length=30, null=False)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField("Активность", default=True)

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.code})'


class Participant(models.Model):
    name = models.CharField("Кличка", max_length=30, null=False)
    color = models.CharField("Окрас", max_length=30, null=True)
    other = models.TextField("Описание", null=True)
    type_p = models.ForeignKey(
        'TypeParticipant', models.RESTRICT, 'participant_type', verbose_name='Вид животного'
    )
    breed = models.ForeignKey(
        'BreedParticipant', models.RESTRICT, 'participant_breed', verbose_name='Порода'
    )
    avatar_id = models.CharField("Аватар", max_length=255, null=False)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'

class Avatar(models.Model):
    foto = models.CharField("Фотография", max_length=255, null=False)
    description = models.CharField("Описание фотографии", max_length=255, null=True)
    participant_id = models.ForeignKey(
        Participant, models.PROTECT, 'participant_foto', verbose_name='ID участника'
    )
    class Meta:
        verbose_name = 'Фотография участника'
        verbose_name_plural = 'Фотографии участника'
        ordering = ('participant_id',)
    def __str__(self):
        return f'{self.participant_id} {self.description} ({self.pk})'