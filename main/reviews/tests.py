from django.test import TestCase

from main.reviews.models import Reviews


# Create your tests here.
class ReviewsModelTestCase(TestCase):
    def setUp(self):
        """Создание объекта Reviews для тестирования"""

        self.reviews = Reviews.objects.create(
            full_name="Test Reviews",
            description="This is a test Reviews",
            img="test_image.jpg"
        )

    def test_read_reviews(self):
        """Тестирование чтения объекта Reviews"""

        # Получаем объект Blog по id
        reviews = Reviews.objects.get(id=self.reviews.id)

        # Проверяем, что объект содержит правильные значения полей
        self.assertEqual(reviews.full_name, "Test Reviews")
        self.assertEqual(reviews.description, "This is a test Reviews")
        self.assertEqual(reviews.img, "test_image.jpg")

    def test_update_reviews(self):
        """Тестирование обновления объекта Reviews"""

        # Обновляем значения полей объекта Blog
        self.reviews.full_name = "Updated Test Doctors"
        self.reviews.description = "This is an updated test Doctors"
        self.reviews.img = "updated_test_Doctors.jpg"
        self.reviews.save()

        # Получаем обновленный объект Blog по id
        updated_reviews = Reviews.objects.get(id=self.reviews.id)

        # Проверяем, что объект был успешно обновлен и содержит правильные значения полей
        self.assertEqual(updated_reviews.full_name, "Updated Test Doctors")
        self.assertEqual(updated_reviews.description, "This is an updated test Doctors")
        self.assertEqual(updated_reviews.img, "updated_test_Doctors.jpg")

    def test_delete_reviews(self):
        """Тестирование удаления объекта Reviews"""

        # Удаляем объект Blog
        self.reviews.delete()

        # Проверяем, что объект был успешно удален
        with self.assertRaises(Reviews.DoesNotExist):
            Reviews.objects.get(id=self.reviews.id)
