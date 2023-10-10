from django.test import TestCase

from main.doctors.models import Doctors


class DoctorsModelTestCase(TestCase):
    def setUp(self):
        """Создание объекта Doctors для тестирования"""

        self.doctors = Doctors.objects.create(
            category_doctor="Test Doctors",
            description="This is a test Doctors",
            image="test_image.jpg"
        )

    def test_read_doctors(self):
        """Тестирование чтения объекта Doctors"""

        # Получаем объект Blog по id
        doctors = Doctors.objects.get(id=self.doctors.id)

        # Проверяем, что объект содержит правильные значения полей
        self.assertEqual(doctors.category_doctor, "Test Doctors")
        self.assertEqual(doctors.description, "This is a test Doctors")
        self.assertEqual(doctors.image, "test_image.jpg")

    def test_update_doctors(self):
        """Тестирование обновления объекта Doctors"""

        # Обновляем значения полей объекта Blog
        self.doctors.category_doctor = "Updated Test Doctors"
        self.doctors.description = "This is an updated test Doctors"
        self.doctors.image = "updated_test_Doctors.jpg"
        self.doctors.save()

        # Получаем обновленный объект Blog по id
        updated_blog = Doctors.objects.get(id=self.doctors.id)

        # Проверяем, что объект был успешно обновлен и содержит правильные значения полей
        self.assertEqual(updated_blog.category_doctor, "Updated Test Doctors")
        self.assertEqual(updated_blog.description, "This is an updated test Doctors")
        self.assertEqual(updated_blog.image, "updated_test_Doctors.jpg")

    def test_delete_doctors(self):
        """Тестирование удаления объекта Doctors"""

        # Удаляем объект Blog
        self.doctors.delete()

        # Проверяем, что объект был успешно удален
        with self.assertRaises(Doctors.DoesNotExist):
            Doctors.objects.get(id=self.doctors.id)
