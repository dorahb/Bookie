from django.db import models

# Create your models here.

class Book(models.Model):
  image = models.ImageField(null=True, blank=True)  
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  synopsis = models.CharField(max_length=1000)

  def __str__(self):
        return self.title
  
  @property
  def imageURL(self):
    try:
      url = self.image.url
    except:
      url = ''
    return url  


class Review(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  comment = models.CharField(max_length=1000)
  votes = models.IntegerField(blank=True,default=0)

  def __str__(self):
        return self.book


