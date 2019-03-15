from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import BlogForm
from .models import Blog
from datetime import datetime
from django.contrib.auth.decorators import login_required

def index(request):
  blog_posts = Blog.objects.all()
  context = {
    "blog_posts": blog_posts
  }
  return render(request, "blog_app/index.html", context)

@login_required(login_url='/login/')
def post_blog(request):
  if request.method == "POST":
    form = BlogForm(request.POST)
    if form.is_valid():
      title = form.cleaned_data.get("title")
      content = form.cleaned_data.get("content")
      blog = Blog.objects.create(title=title, content=content, date=datetime.now(), author_id=request.user.id)
      blog.save()
      return redirect("index")
  else:
      form = BlogForm()
  return render(request, "blog_app/new_blog.html", {"form": form})

def signup(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get("username")
      raw_password = form.cleaned_data.get("password1")
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect("index")
  else:
      form = UserCreationForm()
  return render(request, "blog_app/signup.html", {"form": form})
