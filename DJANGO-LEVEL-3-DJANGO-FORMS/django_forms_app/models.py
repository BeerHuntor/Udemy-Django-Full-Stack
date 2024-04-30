from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, default= '')
    star_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review_content = models.TextField()
>>>>>>> refs/remotes/origin/main
