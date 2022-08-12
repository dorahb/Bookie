from django.db import models

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  synopsis = models.CharField(max_length=1000)

class Review(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  comment = models.CharField(max_length=1000)
  votes = models.IntegerField(default=0)


