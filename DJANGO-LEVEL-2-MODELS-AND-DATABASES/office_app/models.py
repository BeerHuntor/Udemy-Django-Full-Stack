from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    #Adding fields after the model has been created requires a default value for all previous fields already in the database
    heart_rate = models.IntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(300)])

    # Adding entries to the database: Patient.objects.create(first_name='x', last_name = 'x', age = xx)

    # Updating already existing entries in a db. 
    ### Get a patient object. 
    ### carl = Patient.objects.get(pk=1) //sql indexing starts from 1
    ### carl.last_name = 'XXXX'
    ### carl.save()

    # Removing an already existing item from a db. 
    ### same as above
    ### carl.delete()  
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}, and is {self.age} years old!"