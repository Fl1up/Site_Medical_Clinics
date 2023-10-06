from django.core.management.base import BaseCommand

from main.reviews.models import Reviews


class Command(BaseCommand):
    def handle(self, *args, **options):
        Reviews.objects.all().delete(),

        Reviews.objects.create(
            full_name='Джон Смит',
            img="reviews/img_7.png",
            description="Понравилось")
        Reviews.objects.create(
            full_name='Анастасия Бонд',
            img="reviews/img_6.png",
            description="Понравилось")
        Reviews.objects.create(
            full_name='Андрей Кукарев',
            img="reviews/img_5.png",
            description="Понравилось")
        Reviews.objects.create(
            full_name='Томили джонс',
            img="reviews/img_4.png",
            description="Понравилось")
        Reviews.objects.create(
            full_name='Джон Смит',
            img="reviews/img_4.png",
            description="Понравилось")
        Reviews.objects.create(
            full_name='Тамара Фон',
            img="reviews/img_3.png",
            description="Понравилось")
        Reviews.objects.create(
            full_name='Альберт Инштейен',
            img="reviews/img_2.png",
            description="Понравилось")
        Reviews.objects.create(
            full_name='Вася пупкин',
            img="reviews/img_1.png",
            description="Понравилось")
