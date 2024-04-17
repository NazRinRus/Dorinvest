from django.db import models
from exhibition.models import participant, partner


def get_image_path(instance, file):  # прописываю путь сохранения изображений, у каждой выставки Exhibition своя папка
    return f'static/photos/exhibition-{Exhibition.objects.count() + 1}/{file}'


class Exhibition(models.Model):
    ABOUT_EXHIBITION = """При поддержке ГБУ «Доринвест» мы рады пригласить вас на выставку животных, которая проводится с целью пристройства наших пушистых друзей в заботливые дома. Мы гордимся нашими приютами, где животным предоставляются комфортные условия, проходят ветеринарный уход и получают все необходимые прививки и процедуры."""

    name = models.CharField("Название выставки", max_length=30, null=True, default="Ищу друга!")
    description = models.CharField(max_length=250, null=True, verbose_name="Описание выставки",
                                   default="Большая выставка кошек и собак")
    bunner = models.ImageField("Баннер", upload_to=get_image_path, blank=True, null=True)
    date_begin = models.DateField("Дата начала выставки")
    date_end = models.DateField("Дата окончания выставки")
    time_event = models.CharField(max_length=255, null=False, verbose_name="Время проведения выставки")
    location = models.CharField("Место проведения", max_length=30, null=False)
    about = models.TextField(verbose_name="О выставке", default=ABOUT_EXHIBITION)

    participants = models.ManyToManyField(
        participant.Participant,
        related_name='exhibition_participant',
        blank=True,
        verbose_name='Участники',
        through='ExhibitionParticipant'

    )
    partners = models.ManyToManyField(
        partner.Partner,
        related_name='exhibition_partner',
        blank=True,
        verbose_name='Партнеры',
        through='ExhibitionPartner'
    )
    results = models.TextField(null=True, blank=True, verbose_name="Итоги выставки")

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'
        ordering = ('-date_begin', 'name',)

    def __str__(self):
        return f'{self.name} ({self.pk}) {self.date_begin}'


class Foto(models.Model):
    foto = models.ImageField("Фотография", upload_to=get_image_path, blank=True, null=True)
    description = models.CharField("Описание фотографии", max_length=255, null=True, blank=True)
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
        return f'({self.pk}) {self.exhibition_id}'


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
        return f'({self.pk}) {self.exhibition_id}'


class FAQ(models.Model):
    """Модель ответов на часто задаваемые вопросы."""
    question = models.TextField(null=True, verbose_name="Вопрос")
    answer = models.TextField(null=True, verbose_name="Ответ")

    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "Часто задаваемые вопросы"

    def __str__(self):
        return f'{self.question}'


class Feedback(models.Model):
    """Модель заявки на дистанционное приобретение питомца."""
    name = models.CharField(max_length=100, null=True, verbose_name="ФИО отправителя")
    phone = models.CharField(max_length=20, null=True, verbose_name="Телефон отправителя")
    email = models.EmailField(max_length=100, null=True, verbose_name="Эл.почта отправителя")
    participant = models.CharField(max_length=100, null=True, verbose_name="Данные питомца, которого хотят взять")

    def __str__(self):
        return f"({self.name}) ({self.email})"

    class Meta:
        verbose_name = "Заявка на приобретение питомца"
        verbose_name_plural = "Заявки на приобретение питомца"
