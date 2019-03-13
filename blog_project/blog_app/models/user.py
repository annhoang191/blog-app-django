from django.db import models

class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=200)
  password = models.CharField(max_length=50)
  avatar = models.CharField(max_length=500, null=True)

  def __str__(self):
    return self.name
