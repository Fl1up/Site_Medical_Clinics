from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from main.reviews.models import Reviews


class ReviewsCreateView(CreateView):
    model = Reviews


class ReviewsListView(ListView):
    model = Reviews
    template_name = "reviews_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавление контекстных данных в словарь
        context['reviews'] = 'reviews'
        return context


class ReviewsUpdateView(UpdateView):
    model = Reviews
    success_url = reverse_lazy('reviews:list')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)


class ReviewsDetailView(DetailView):
    model = Reviews
    template_name = "reviews_detail.html"


class ReviewsDeleteView(DeleteView):
    model = Reviews
    success_url = reverse_lazy('reviews:list')
