from django.db import models
from django.core.exceptions import ValidationError
import datetime

def validate_main(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This filed only aaccpt gamil...")

# Create your models here.
'''
class student(models.Model):
    #? Built-in Field Validations in Django models are the validations 
    #? that come predefined to all Django fields. Every field comes in 
    #? with built-in validations from Django validators.
    
    # todo --> Attributes
    # NULL = True  # !---> Django will allow empty values to store
    # blank= True # !---> Will allow to keep the field empty
    # db_column = 'Name' # ! ---> The name of the database column to use for this field
    # db_index = True # ! database index will be created for this 
    # default="some value" # ! ---> The default value for the field.
    # help_text = "text" # ! --> Eg: help_text="Please use the following format: <em>YYYY-MM-DD</em>".
    # primary_key=True
    # editable = False # ! ---> default is True --> If False, the field will not be displayed in the 
    # !admin or any other ModelForm.
    # unique = True # ! --> used to keep the field unique
    # error_message = # ! --> The error_messages argument lets you override the 
    # default messages that the field will raise. Pass in a dictionary with 
    # keys matching the error messages you want to override.
    # *  error_message Eg: 
    # class GeeksModel(Model):
    #                 geeks_field = models.CharField(
    #                 max_length = 200,  
    #                 unique = True,
    #                 error_messages ={
    #                 "unique":"The Geeks Field you entered is not unique."
    #                 }
    #                 )
    # verbose_name = "name" #!---> verbose_name is a human-readable name for the field. 
    
    name = models.CharField(Null=True, blank=True, db_column="Usr_name", db_index=True, default=None, unique=True, error_message={"unique":"Field you entered is not unique"}, verbose_name="Username")
    age = models.IntegerField()  # ! ---> It supports values from -2147483648 to 2147483647 are safe in all databases supported by Django.
    date_created  = models.DateField(auto_now_add=True)
    last_updates = models.DateField(auto_now=True)
    date = models.DateField()
    # auto_now_add --> auto_now_add sets the field's date only when you create the data.
    # auto_now -->auto_now parameter sets the date every time you change or update data.
    
    date_time = models.DateTimeField() # !--> same parameter as DateField 
    date_time = models.DateTimeField(default = datetime.now, blank = True)
    salary = models.DecimalField( 
                         max_digits = 5, 
                         decimal_places = 2)
    email_field = models.EmailField(max_length = 254, validators =[validate_main])
    average = models.FloatField()
    Ip = models.GenericIPAddressField() # ! -->(e.g. 192.0.2.30 or 2a02:42fe::4)
    feedback = models.TextField()
    status = models.BooleanField(default=True)
    weblink = models.URLField(max_length = 200)
'''

class employee(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="pics")
    upload = models.FileField()   
     
    def __str__(self):
        return self.name
    
class std1(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.CharField(max_length = 70)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    
    
    
    