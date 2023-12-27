from django.db import models

# Create your models here.

class Employee(models.Model):
    E_name = models.CharField(max_length=30)
    E_id = models.CharField(max_length=20, unique=True, blank=False)
    E_email = models.EmailField()
    E_salary = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.E_name