from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    # Create relationship, (don't inherity from User!)
    user = models.OneToOneField(User)

    # Add any additional attributes you want. 
    user_portfolio = models.URLField(blank=True, max_length=200)
    user_profile_image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username