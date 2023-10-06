from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from main.blog.models import Blog
from main.doctors.forms import DoctorsForms
from main.doctors.models import Doctors
from main.reviews.models import Reviews
from main.shop.models import Shop


# Create your views here
# Основа

# Доктора

class DoctorsCreateView(CreateView):
    model = Shop
    form_class = DoctorsForms
    success_url = reverse_lazy('doctors:list')


class DoctorsListView(ListView):
    model = Doctors
    template_name = "doctors/doctors_list.html"


class DoctorsDetailView(DetailView):
    model = Doctors
    template_name = "doctors/doctors_detail.html"


class DoctorsDeleteView(DeleteView):
    model = Doctors
    success_url = reverse_lazy('doctors:list')


class DoctorsUpdateView(UpdateView):
    model = Doctors
    form_class = DoctorsForms
    success_url = reverse_lazy('doctors:list')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.full_name)
            new_art.save()
        return super().form_valid(form)

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
