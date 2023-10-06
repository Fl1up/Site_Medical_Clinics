from django import forms

from main.shop.models import Shop


class ShopForms(forms.ModelForm):

    class Meta:
        model = Shop
        fields = '__all__'
