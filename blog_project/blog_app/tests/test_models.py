from django.test import TestCase
from blog_app.models import Blog
from django.contrib.auth.models import User
from datetime import datetime

class BlogModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    User.objects.create_user(username="test", password="Aa@123456")
    Blog.objects.create(title="test", content="123456abc", author_id=1, date=datetime.now())

  def test_title_max_length(self):
    blog = Blog.objects.get(id=1)
    max_length = blog._meta.get_field("title").max_length
    self.assertEquals(max_length, 64)

  def test_content_max_length(self):
    blog = Blog.objects.get(id=1)
    max_length = blog._meta.get_field("content").max_length
    self.assertEquals(max_length, 2500)
