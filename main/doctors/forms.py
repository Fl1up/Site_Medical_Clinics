from django import forms

from main.doctors.models import Doctors


class DoctorsForms(forms.ModelForm):

    class Meta:
        model = Doctors
        fields = '__all__'
