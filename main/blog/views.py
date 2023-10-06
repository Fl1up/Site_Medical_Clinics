from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from main.blog.forms import BlogForms
from main.blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForms
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавление контекстных данных в словарь
        context['shop'] = 'shop'
        return context


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForms
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
