from django import forms
from main.forms import StyleFormMixin
from blog.models import Blog


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('slug', 'is_published', 'views_count')
