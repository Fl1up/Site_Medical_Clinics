from django import forms

from main.blog.models import Blog


class BlogForms(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
