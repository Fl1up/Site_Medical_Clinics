from django.test import TestCase
from main.blog.models import Blog


class BlogModelTestCase(TestCase):
    def setUp(self):
        """Создание объекта Blog для тестирования"""

        self.blog = Blog.objects.create(
            title="Test Blog",
            description="This blog",
            img="test_image.jpg"
        )

    def test_read_blog(self):
        """Тестирование чтения объекта Blog"""

        # Получаем объект Blog по id
        blog = Blog.objects.get(id=self.blog.id)

        # Проверяем, что объект содержит правильные значения полей
        self.assertEqual(blog.title, "Test Blog")
        self.assertEqual(blog.description, "This blog")
        self.assertEqual(blog.img, "test_image.jpg")

    def test_update_blog(self):
        """Тестирование обновления объекта Blog"""

        # Обновляем значения полей объекта Blog
        self.blog.title = "Updated Test Blog"
        self.blog.description = "This is an updated test blog"
        self.blog.img = "updated_test_image.jpg"
        self.blog.save()

        # Получаем обновленный объект Blog по id
        updated_blog = Blog.objects.get(id=self.blog.id)

        # Проверяем, что объект был успешно обновлен и содержит правильные значения полей
        self.assertEqual(updated_blog.title, "Updated Test Blog")
        self.assertEqual(updated_blog.description, "This is an updated test blog")
        self.assertEqual(updated_blog.img, "updated_test_image.jpg")

    def test_delete_blog(self):
        """Тестирование удаления объекта Blog"""

        # Удаляем объект Blog
        self.blog.delete()

        # Проверяем, что объект был успешно удален
        with self.assertRaises(Blog.DoesNotExist):
            Blog.objects.get(id=self.blog.id)
