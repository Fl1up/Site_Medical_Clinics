from django.test import TestCase

from main.users.models import User


# Create your tests here.
class UserModelTestCase(TestCase):
    def setUp(self):
        """Создание объекта User для тестирования"""

        self.user = User.objects.create(
            email="Test_mail@mail.ru",

        )

    def test_read_user(self):
        """Тестирование чтения объекта User"""

        # Получаем объект Blog по id
        user = User.objects.get(id=self.user.id)

        # Проверяем, что объект содержит правильные значения полей
        self.assertEqual(user.email, "Test_mail@mail.ru")

    def test_update_user(self):
        """Тестирование обновления объекта User"""

        # Обновляем значения полей объекта Blog
        self.user.email = "Test_mail_1@mail.ru"

        self.user.save()

        # Получаем обновленный объект Blog по id
        user = User.objects.get(id=self.user.id)

        # Проверяем, что объект был успешно обновлен и содержит правильные значения полей
        self.assertEqual(user.email, "Test_mail_1@mail.ru")

    def test_delete_user(self):
        """Тестирование удаления объекта User"""

        # Удаляем объект Blog
        self.user.delete()

        # Проверяем, что объект был успешно удален
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)
