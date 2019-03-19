from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

urlpatterns = [
  path("", views.index, name="index"),
  path("signup", views.signup, name="signup"),
  url(r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
    views.activate, name="activate"),
  url(r"^login/$", auth_views.LoginView.as_view(template_name="blog_app/login.html"), name="login"),
  url(r"^logout/$", auth_views.LogoutView.as_view(), {"next_page": "/"}, name="logout"),
  path("blog/new", views.post_blog, name="new_blog"),
  path("blog/<int:id>", views.blog_detail, name="blog_detail"),
  path("blog/<int:id>/edit", views.blog_edit, name="blog_edit"),
  path("blog/<int:id>/delete", views.blog_delete, name="blog_delete")
]
