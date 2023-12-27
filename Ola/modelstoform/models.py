from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=30, blank =False)
    age = models.IntegerField()
    emp_id=models.CharField(max_length=10, blank=True, unique=True)
    image = models.ImageField(upload_to="pics")
    salary=models.FloatField(default=0.0)

    def __str__(self):
        return self.name