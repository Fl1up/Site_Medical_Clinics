from django.test import TestCase

from main.shop.models import Shop


# Create your tests here.
class ShopModelTestCase(TestCase):
    def setUp(self):
        """Создание объекта Shop для тестирования"""

        self.shop = Shop.objects.create(
            name_product="Test shop",
            description="This is a test shop",
            image="test_image.jpg",
            prise=1000
        )

    def test_read_shop(self):
        """Тестирование чтения объекта Shop"""

        # Получаем объект Blog по id
        shop = Shop.objects.get(id=self.shop.id)

        # Проверяем, что объект содержит правильные значения полей
        self.assertEqual(shop.name_product, "Test shop")
        self.assertEqual(shop.description, "This is a test shop")
        self.assertEqual(shop.image, "test_image.jpg")
        self.assertEqual(shop.prise, 1000)

    def test_update_shop(self):
        """Тестирование обновления объекта Shop"""

        # Обновляем значения полей объекта Blog
        self.shop.name_product = "Updated Test shop"
        self.shop.description = "This is an updated test shop"
        self.shop.image = "updated_test_shop.jpg"
        self.shop.prise = 1100
        self.shop.save()

        # Получаем обновленный объект Blog по id
        updated_shop = Shop.objects.get(id=self.shop.id)

        # Проверяем, что объект был успешно обновлен и содержит правильные значения полей
        self.assertEqual(updated_shop.name_product, "Updated Test shop")
        self.assertEqual(updated_shop.description, "This is an updated test shop")
        self.assertEqual(updated_shop.image, "updated_test_shop.jpg")
        self.assertEqual(updated_shop.prise, 1100)

    def test_delete_shop(self):
        """Тестирование удаления объекта Shop"""

        # Удаляем объект Blog
        self.shop.delete()

        # Проверяем, что объект был успешно удален
        with self.assertRaises(Shop.DoesNotExist):
            Shop.objects.get(id=self.shop.id)
