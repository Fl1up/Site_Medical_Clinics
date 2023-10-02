from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from main.blog.models import Blog
from main.doctors.models import Doctors
from main.reviews.models import Reviews
from main.shop.models import Shop


# Create your views here
# Основа

# Доктора
class DoctorsListView(ListView):
    model = Doctors
    template_name = "doctors_list.html"


class DoctorsDetailView(DetailView):
    model = Doctors
    template_name = "doctors_detail.html"


# Контакты
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    context = {
        'title': "Контакты"
    }
    return render(request, 'contact.html', context)


def main(request):
    shop = Shop.objects.all()
    doctors = Doctors.objects.all()
    reviews = Reviews.objects.all()
    blog = Blog.objects.all()

    context = {
        'doctors': doctors,
        'shop': shop,
        "reviews": reviews,
        "blog": blog,
    }
    return render(request, 'main_list.html', context)