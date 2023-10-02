from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.doctors.apps import DoctorsConfig
from main.doctors.views import DoctorsListView, contact, DoctorsDetailView, main

app_name = DoctorsConfig.name

urlpatterns = [
    path("", main, name="main"),
    path("doctors/", DoctorsListView.as_view(), name="list"),
    path("contact/", contact, name="contact"),
    path('view/<int:pk>', DoctorsDetailView.as_view(), name='view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)