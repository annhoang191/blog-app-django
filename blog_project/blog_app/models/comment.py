from django.db import models
from django.contrib.auth.models import User
from .blog import Blog

class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  commented_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
  content = models.TextField(max_length=2500)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.content
