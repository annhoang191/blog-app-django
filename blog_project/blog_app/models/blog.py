from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
  title = models.CharField(max_length=64)
  date = models.DateTimeField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField(max_length=2500)

  def __str__(self):
    return self.title
