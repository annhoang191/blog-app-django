from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=64, label="Title", widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(max_length=2500, label="Content", widget=forms.Textarea(attrs={"class": "form-control"}))
