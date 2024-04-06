from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    # Adding fields after the model has been created requries an default value for all previous fields already in the DB
    heart_rate = models.IntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(300)]) 
    

    def __str__(self):
        return f"{self.last_name}, {self.first_name}, and is {self.age} years old!"