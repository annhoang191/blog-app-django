from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import BlogForm
from .models import Blog
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
  blog_posts = Blog.objects.all().order_by("-date")
  paginator = Paginator(blog_posts, 5)
  page = request.GET.get("page")
  blog_posts = paginator.get_page(page)
  return render(request, "blog_app/index.html", {'blog_posts': blog_posts})

def blog_detail(request, id):
  blog = get_object_or_404(Blog, id=id)
  return render(request, "blog_app/blog_detail.html", {"blog": blog})

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

def blog_edit(request, id):
  blog = get_object_or_404(Blog, id=id)
  if request.method == "POST":
    form = BlogForm(request.POST, instance=blog)
    if request.user == blog.author and form.is_valid():
      blog = form.save(commit=False)
      blog.author = request.user
      blog.save()
      return redirect("blog_detail", id=blog.id)
  else:
    form = BlogForm(instance=blog)
  return render(request, "blog_app/new_blog.html", {"form": form})

def blog_delete(request, id):
  blog = get_object_or_404(Blog, id=id)
  blog.delete()
  return redirect("index")

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
