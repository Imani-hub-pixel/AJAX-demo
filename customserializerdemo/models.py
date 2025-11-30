from django.db import models

# Create your models here.
class UserName(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=200)
    comments=models.TextField()
    created_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content=models.TextField(max_length=300)
    author=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)
