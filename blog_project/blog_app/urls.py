from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

urlpatterns = [
  path("", views.index, name="index"),
  path("signup", views.signup, name="signup"),
  url(r"^login/$", auth_views.LoginView.as_view(template_name="blog_app/login.html"), name="login"),
  url(r"^logout/$", auth_views.LogoutView.as_view(), {"next_page": "/"}, name="logout"),
  path("blog/new", views.post_blog, name="new_blog")
]
