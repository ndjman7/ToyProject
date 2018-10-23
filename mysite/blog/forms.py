from django import forms
from .models import Blog

# class BlogForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     title_description = forms.CharField(max_length=200)
#     content = forms.CharField(widget=forms.Textarea)
#     is_published = forms.BooleanField()


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['user', ]
