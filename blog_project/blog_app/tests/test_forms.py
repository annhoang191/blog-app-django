from django.test import TestCase
from blog_app.forms import BlogForm

class BlogFormTest(TestCase):
  def test_title_label(self):
    form = BlogForm()
    self.assertTrue(form.fields["title"].label == "Title")

  def test_form_data_valid(self):
    title = "test"
    content = "abc123456"
    form = BlogForm(data={"title": title, "content": content})
    self.assertTrue(form.is_valid())
