from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.doctors.apps import DoctorsConfig
from main.doctors.views import DoctorsListView, contact, DoctorsDetailView, main, \
    DoctorsDeleteView, DoctorsUpdateView, DoctorsCreateView

app_name = DoctorsConfig.name

urlpatterns = [
    path("", main, name="main"),

    path("doctors/", DoctorsListView.as_view(), name="list"),
    path("create/", DoctorsCreateView.as_view(), name="create"),
    path('view/<int:pk>', DoctorsDetailView.as_view(), name='view'),
    path('edit/<int:pk>', DoctorsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', DoctorsDeleteView.as_view(), name='delete'),

    #  contact
    path("contact/", contact, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
