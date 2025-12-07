from django.db import models

# Create your models here.
class BookGenre(models.Model):
    name=models.CharField(max_length=100)
class Book(models.Model):
    title=models.CharField(max_length=200) 
    author_name=models.CharField(max_length=200)
    genre=models.ForeignKey(BookGenre,on_delete=models.CASCADE)
    created_at=models.DateTimeField()







