from django.db import models

# ? ORM --> Object Relational Mapping
# ? To Create Database quries on seeing modesl class
# ---> python manage.py makemigrations
# ? To execute the database quries create by migration command
# ---> python manage.py migrate


# class student(models.Model):
#     Name = models.CharField(max_length=50)
#     rollnum = models.CharField(max_length=20, unique=True)
#     age = models.IntegerField()
#     email = models.EmailField()
    
#     def __str__(self):
#         return self.Name
    
# gender = (
#     ("M", "Male"),
#     ("F", "Female"),
#     ("O", "Others")
# )

# import datetime
# class typeoffields(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     average = models.DecimalField(max_digits=6, decimal_places=2)
#     date_created = models.DateField(auto_now_add=True)
#     # auto_now_add = sets the date when u 
#     # created the field
#     # auto_now = sets the date when u 
#     # modified the field    
#     date_time = models.DateTimeField(default=datetime.datetime.now())
#     email = models.EmailField()
#     feedback = models.TextField()
#     status = models.BooleanField(default=False)
#     weblinks = models.URLField(max_length=250)
#     Ip = models.GenericIPAddressField()
#     salary = models.FloatField()
#     Gender = models.CharField(max_length=10, choices=gender)
    

#     def __str__(self):
#         return self.name

# # To store images or other files
# class employee(models.Model):
#     name = models.CharField(max_length=30)
#     image = models.ImageField(upload_to='pics')

#     def __str__(self):
#         return self.name
    
# class staff(models.Model):
#     docs = models.FileField()
#     name = models.CharField(max_length=30)
    
#     def __str__(self):
#         return self.name
    
# Attributes of Model field methods
# ? blank = True #! it allow the field to be empty
# ? db_column = "name" # Giving another name 
# to field at backend
# ? verbose_name = "name" --> change the field 
# display name in db
# help_text
# default
# primary_key
# unique
# required
# error_message
# validator


# class stud(models.Model):
#     name = models.CharField(max_length=30, blank=True)
#     age= models.IntegerField(verbose_name="AGE_of_fog")
#     password = models.CharField(max_length=40, help_text="Plesae enter more than 8 char")

#     def __str__(self):
#         return self.name
    
