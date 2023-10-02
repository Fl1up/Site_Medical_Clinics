from main.shop.apps import ShopConfig
from django.urls import path

from main.shop.views import ShopCreateView, ShopDeleteView, ShopListView, ShopUpdateView, ShopDetailView

app_name = ShopConfig.name

urlpatterns = [
    path('create/', ShopCreateView.as_view(), name='create'),
    path('', ShopListView.as_view(), name='list'),
    path('view/<int:pk>', ShopDetailView.as_view(), name='view'),
    path('edit/<int:pk>', ShopUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ShopDeleteView.as_view(), name='delete'),
]