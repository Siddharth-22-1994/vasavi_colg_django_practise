from django.db import models

# Create your models here.

class blog(models.Model):
    name = models.CharField(max_length=20)
    tagline = models.TextField()
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Enrty(models.Model):
    blog= models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blog_data')
    headline = models.CharField(max_length=20)
    pub_date = models.DateField()
    body_text=models.TextField()
    authors = models.ManyToManyField(Author, related_name='author')
    rating = models.IntegerField()
    
    def __str__(self):
        return self.headline 
    
    