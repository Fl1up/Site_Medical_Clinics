from main.reviews.apps import ReviewsConfig
from django.urls import path

from main.reviews.views import ReviewsCreateView, ReviewsListView, ReviewsDetailView, ReviewsUpdateView, \
    ReviewsDeleteView

app_name = ReviewsConfig.name

urlpatterns = [
    path('create/', ReviewsCreateView.as_view(), name='create'),
    path('', ReviewsListView.as_view(), name='list'),
    path('view/<int:pk>', ReviewsDetailView.as_view(), name='view'),
    path('edit/<int:pk>', ReviewsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ReviewsDeleteView.as_view(), name='delete'),
]
