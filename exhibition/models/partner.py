from django.db import models


def get_image_path(instance, file): # прописываю путь сохранения изображений, у каждого партнера Partner своя папка
    return f'static/photos/partner-{Partner.objects.last().id}/{file}'


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
