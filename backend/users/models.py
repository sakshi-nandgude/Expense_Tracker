from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # You can add additional fields here if needed
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"] 
    
    def __str__(self):
        return self.email 
         # Keep username as a required field for compatibility with Django's auth system