from django.db import models

class book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    publication = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.title