from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


# Create your models here.
class Reviews(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Полное имя")
    description = models.CharField(max_length=150, verbose_name="Описание")
    img = models.ImageField(verbose_name="Фото", **NULLABLE)

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


# Create your models here.
