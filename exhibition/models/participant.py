from django.db import models


def get_image_path(instance,
                   file):  # прописываю путь сохранения изображений, у каждого участника Participant своя папка
    last_participant = Participant.objects.last()
    if last_participant is not None:
        return f'static/photos/participant-{last_participant.id}/{file}'
    else:
        # Обработка случая, когда последний участник не найден
        return f'static/photos/participant-0/{file}'


class TypeParticipant(models.Model):
    code = models.CharField('Код', max_length=10, primary_key=True)
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


class TalentParticipant(models.Model):
    code = models.CharField('Код', max_length=3, primary_key=True)
    name = models.CharField("Талант", max_length=60, null=False)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField("Активность", default=True)

    class Meta:
        verbose_name = 'Талант'
        verbose_name_plural = 'Таланты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.code})'


class Participant(models.Model):
    GENDER = [
        ('boy', 'Мальчик'),
        ('girl', 'Девочка'),
    ]

    name = models.CharField("Кличка", max_length=30, null=False)
    color = models.CharField("Окрас", max_length=30, null=True, blank=True)
    age = models.CharField("Возраст", max_length=30, null=True, blank=True)
    gender = models.CharField("Пол", max_length=10, choices=GENDER)
    other = models.TextField("Описание", null=True)
    found_home = models.BooleanField(default=False, verbose_name="Забрали домой")
    type_p = models.ForeignKey(
        'TypeParticipant', models.RESTRICT, 'participant_type', verbose_name='Вид животного'
    )
    breed = models.ForeignKey(
        'BreedParticipant', models.RESTRICT, 'participant_breed', verbose_name='Порода'
    )
    talent = models.ForeignKey(
        'TalentParticipant', models.RESTRICT, 'participant_talent', verbose_name='Талант'
    )
    avatar_id = models.ImageField("Аватар", upload_to=get_image_path, blank=True, null=True)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Avatar(models.Model):
    foto = models.ImageField("Фотография", upload_to=get_image_path, blank=True, null=True)
    description = models.CharField("Описание фотографии", max_length=255, null=True, blank=True)
    participant_id = models.ForeignKey(
        Participant, models.PROTECT, 'participant_foto', verbose_name='ID участника'
    )

    class Meta:
        verbose_name = 'Фотография участника'
        verbose_name_plural = 'Фотографии участника'
        ordering = ('participant_id',)

    def __str__(self):
        return f'{self.participant_id} {self.description} ({self.pk})'
