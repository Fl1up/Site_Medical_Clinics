from django.core.management.base import BaseCommand

from main.reviews.models import Reviews


class Command(BaseCommand):
    def handle(self, *args, **options):
        Reviews.objects.all().delete(),

        Reviews.objects.create(full_name='Джон Смит', img="doctors/хирург.png", description="Понравилось")
        Reviews.objects.create(full_name='Томили джонс', img="doctors/хирург.png", description="Понравилось")