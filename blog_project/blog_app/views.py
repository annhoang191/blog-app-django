import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.contrib.auth import login, authenticate
from .forms import BlogForm, SignupForm, CommentForm
from .models import Blog, Comment
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site

def index(request):
  blog_posts = Blog.objects.all().order_by("-date")
  paginator = Paginator(blog_posts, 5)
  page = request.GET.get("page")
  blog_posts = paginator.get_page(page)
  return render(request, "blog_app/index.html", {"blog_posts": blog_posts})

def blog_detail(request, id):
  blog = get_object_or_404(Blog, id=id)
  if blog:
    comments = blog.comment_set.all().order_by("-created")
  form = CommentForm(request.POST or None)
  if request.method == "POST":
    response_data = {}
    content = request.POST.get("content")
    comment = Comment(content=content, author_id=request.user.id, commented_blog=blog, created=datetime.now())
    comment.save()
    response_data["result"] = "Create post successful!"
    response_data["content"] = comment.content
    response_data["created"] = comment.created.strftime("%B %d, %Y %I:%M %p")
    response_data["author"] = comment.author.username
    return HttpResponse(
      json.dumps(response_data),
      content_type="application/json"
    )
    # if form.is_valid():
    #   comment = Comment.objects.create(content=content, author_id=request.user.id, commented_blog=blog, created=datetime.now())
    #   comment.save()
    #   return redirect(request.path)
  return render(request, "blog_app/blog_detail.html", {"blog": blog, "form": form, "comments":comments})

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def blog_delete(request, id):
  blog = get_object_or_404(Blog, id=id)
  blog.delete()
  return redirect("index")

def signup(request):
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_active = False
      user.save()
      current_site = get_current_site(request)
      mail_subject = "Activate your blog account."
      message = render_to_string("blog_app/acc_active_email.html", {
          "user": user,
          "domain": current_site.domain,
          "uid":urlsafe_base64_encode(force_bytes(user.pk)).decode(),
          "token":account_activation_token.make_token(user),
      })
      to_email = form.cleaned_data.get("email")
      email = EmailMessage(mail_subject, message, to=[to_email])
      email.send()
      return HttpResponse("Please confirm your email address to complete the registration")
  else:
    form = SignupForm()
  return render(request, "blog_app/signup.html", {"form": form})

def activate(request, uidb64, token):
  try:
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
  except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    user = None
  if user is not None and account_activation_token.check_token(user, token ):
    user.is_active = True
    user.save()
    login(request, user)
    return HttpResponse("Thank you for your email confirmation. Now you can login your account.")
  else:
    return HttpResponse("Activation link is invalid!")
