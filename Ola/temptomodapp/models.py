from django.db import models
from django.core.exceptions import ValidationError


def gender_validate(txt):
    if txt=="M" or txt=="F":
        return txt
    else:
        raise ValidationError("Please enter Proper gender")
    
def phone_verify(num):
    for val in num:
        if not val.isdigit():
            raise ValidationError("Enter only numbers")
    else:
        return num

class staff_model(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()
    Gender= models.CharField(max_length=10, help_text="Please Enter M for Male, F for Female", validators=[gender_validate])
    phone=models.CharField(max_length=50, validators=[phone_verify])
    image=models.ImageField(upload_to="pics")
    
    def __str__(self):
        return self.name
    
    