from django import forms
from django.forms import ModelForm, Textarea, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog


class BlogForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = ("title", "content")
    widgets = {
      "title": TextInput(attrs={"class": "form-control"}),
      "content": Textarea(attrs={"class": "form-control"})
    }

class SignupForm(UserCreationForm):
  email = forms.EmailField(max_length=100, help_text="Required", widget=forms.TextInput(attrs={"class": "form-control"}))
  password1 = forms.CharField(label="Password", max_length=16, widget=forms.PasswordInput(attrs={"class": "form-control"}))
  password2 = forms.CharField(label="Password Confirmation", max_length=16, widget=forms.PasswordInput(attrs={"class": "form-control"}))
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")
    widgets = {
      "username": TextInput(attrs={"class": "form-control"})
    }
