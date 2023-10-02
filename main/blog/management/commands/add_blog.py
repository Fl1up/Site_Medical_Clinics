from django.core.management.base import BaseCommand

from main.blog.models import Blog


class Command(BaseCommand):
    def handle(self, *args, **options):
        Blog.objects.all().delete(),

        Blog.objects.create(title='Хиру1231231231рг', img="blog/blog_1.png", description="qwdq212312312312wwqdqwdqwd")
        Blog.objects.create(title='Хиsdsdvsdvsvг', img="doctors/хирург.png", description="qwdq212312312312wwqdqwdqwd")
        Blog.objects.create(title='111111111231рг', img="doctors/хирург.png", description="qwdq212312312312wwqdqwdqwd")