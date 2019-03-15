FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_blog_project
WORKDIR /django_blog_project
COPY requirements.txt /django_blog_project/
RUN pip install -r requirements.txt
COPY . /django_blog_project/
