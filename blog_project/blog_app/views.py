from django.shortcuts import render
from django.http import Http404

def index(request):
  return render(request, "blog_app/index.html")
