from django.db import models


def get_image_path(instance, file):  # прописываю путь сохранения изображений, у каждого партнера Partner своя папка
    last_partner = Partner.objects.last()
    if last_partner is not None:
        return f'static/photos/partner-{last_partner.id}/{file}'
    else:
        # Обработка случая, когда последний партнер не найден
        return f'static/photos/partner-0/{file}'


class Partner(models.Model):
    name = models.CharField("Имя партнера", max_length=30, null=False)
    logo = models.ImageField("Логотип", upload_to=get_image_path, blank=True, null=True)
    info = models.TextField("Описание партнера", blank=True, null=True)
    website = models.CharField("Ссылка на вебресурс", max_length=255, null=True)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'
