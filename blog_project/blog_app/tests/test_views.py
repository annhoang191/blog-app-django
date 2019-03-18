from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog_app.models import Blog
from blog_app import views
from datetime import datetime

class HomePageTest(TestCase):
  def test_index_status_code(self):
    response = self.client.get("/")
    self.assertEquals(response.status_code, 200)

  def test_view_url_by_name(self):
    response = self.client.get(reverse("index"))
    self.assertEquals(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse("index"))
    self.assertTemplateUsed(response, "blog_app/index.html")

class BlogIndexTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    number_of_posts = 10
    user = User.objects.create_user(username="test", password="Aa@123456")
    for i in range(number_of_posts):
      Blog.objects.create(
        title = f"Blog post number {i}",
        content = "abc123456",
        author_id = user.id,
        date = datetime.now()
      )

  def test_create_post(self):
    response = self.client.get(reverse("new_blog"))
    self.assertEqual(response.status_code, 302)
    self.client.login(username="test", password="Aa@123456")
    response = self.client.get(reverse("new_blog"))
    self.assertEqual(response.status_code, 200)

  def test_entries_template_context(self):
    response = self.client.get(reverse("index"))
    self.assertEqual(len(response.context["blog_posts"]), 5)

  def test_invalid_post_create(self):
    self.client.login(username="test", password="Aa@123456")
    data = {"title": "title blog post"}
    response = self.client.post(reverse("new_blog"), data)
    self.assertEqual(response.status_code, 200)
    self.assertFormError(response, "form", "content", "This field is required.")

  def test_valid_post_create(self):
    user = User.objects.create_user(username="test1", password="Aa@123456")
    self.client.login(username="test", password="Aa@123456")
    data = {"text": "Test text", "title": "Test title", "date": datetime.now()}
    data["author_id"] = user.id
    self.assertEqual(Blog.objects.count(), 10)
    response = self.client.post(reverse("new_blog"), data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(Blog.objects.count(), 11)
