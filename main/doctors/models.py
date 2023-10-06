from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


# Create your models here.
class Doctors(models.Model):
    category_doctor = models.CharField(
        max_length=100, verbose_name="Категория доктора")
    full_name = models.CharField(
        max_length=100,
        verbose_name="Имя доктора",
        **NULLABLE)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Фото", **NULLABLE)

    def __str__(self):
        return f"{self.category_doctor}, {self.full_name}"

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"
