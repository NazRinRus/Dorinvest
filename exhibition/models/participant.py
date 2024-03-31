from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TypeParticipant(models.Model):
    code = models.CharField('Код', max_length=3, primary_key=True)
    name = models.CharField("Вид животного", max_length=30, null=False)
    sort = models.PositiveSmallIntegerField('Сортировка', max_length=32, null=True, blank=True)
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
    sort = models.PositiveSmallIntegerField('Сортировка', max_length=32, null=True, blank=True)
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
        'exhibilition.TypeParticipant', models.RESTRICT, 'participant_type', verbose_name='Вид животного'
    )
    breed = models.ForeignKey(
        'exhibilition.BreedParticipant', models.RESTRICT, 'participant_breed', verbose_name='Порода'
    )

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'