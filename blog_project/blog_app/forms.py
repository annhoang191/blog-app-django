from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import Blog


class BlogForm(forms.ModelForm):
  # title = forms.CharField(max_length=64, label="Title", widget=forms.TextInput(attrs={"class": "form-control"}))
  # content = forms.CharField(max_length=2500, label="Content", widget=forms.Textarea(attrs={"class": "form-control"}))
  class Meta:
    model = Blog
    fields = ("title", "content")
    widgets = {
      "title": TextInput(attrs={'class': "form-control"}),
      "content": Textarea(attrs={"class": "form-control"})
    }
