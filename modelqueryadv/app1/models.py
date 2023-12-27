from django.db import models

# link --> https://atharvashah.netlify.app/posts/tech/django-orm-exercises/

# Create your models here.
class Author(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=30, null=True)
    zipcode=models.IntegerField(null=True)
    telephone=models.CharField(max_length=30)
    recommendedby=models.ForeignKey("Author", on_delete=models.CASCADE, related_name="recommended_authors", related_query_name="recommended_author", null=True)
    joindate = models.DateField()
    popularity_score = models.IntegerField()
    followers = models.ManyToManyField("User", related_name="followed_authors", related_query_name="followed_authors")
    
    def __str__(self):
        return self.firstname+' '+self.lastname
    
class Books(models.Model):
    title= models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    price=models.IntegerField(null=True)
    published_date = models.DateField()
    author = models.ForeignKey()