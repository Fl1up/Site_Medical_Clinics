from django.db import models

from main.doctors.models import NULLABLE


class Shop(models.Model):
    name_product = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Фото", **NULLABLE)
    prise = models.IntegerField(default=0, verbose_name="Цена")

    def __str__(self):
        return f"{self.name_product} {self.prise}"

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
