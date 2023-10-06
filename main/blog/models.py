from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Полное имя")
    description = models.CharField(max_length=550, verbose_name="Описание")
    img = models.ImageField(verbose_name="Фото")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
