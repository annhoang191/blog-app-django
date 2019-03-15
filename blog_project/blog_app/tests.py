from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse
from . import views

class HomePageTest(SimpleTestCase):
  def test_index_status_code(self):
    response = self.client.get("/")
    self.assertEquals(response.status_code, 200)

  def test_view_url_by_name(self):
    response = self.client.get(reverse("index"))
    self.assertEquals(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse("index"))
    self.assertTemplateUsed(response, "blog_app/index.html")
