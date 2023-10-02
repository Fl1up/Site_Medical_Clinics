from pytils.translit import slugify
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from main.shop.models import Shop


class ShopCreateView(CreateView):
    model = Shop


class ShopListView(ListView):
    model = Shop
    template_name = "shop_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавление контекстных данных в словарь
        context['shop'] = 'shop'
        return context


class ShopUpdateView(UpdateView):
    model = Shop
    success_url = reverse_lazy('shop:list')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()
        return super().form_valid(form)



class ShopDetailView(DetailView):
    model = Shop
    template_name = "shop_detail.html"


class ShopDeleteView(DeleteView):
    model = Shop
    success_url = reverse_lazy('shop:list')