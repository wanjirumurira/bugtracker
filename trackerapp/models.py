from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
import uuid
#AbstractUser: Use this option if you are happy with the existing fields on the 
# User model and just want to remove the username field.

# Create your models here.
class User(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return self.username

class Project(models.Model):
    project_name = models.CharField(max_length=150,unique=True)
    description = models.TextField(blank=True)
    contributors = models.ManyToManyField(User,related_name="contributors")
    create_at = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.project_name

class BugTicket(models.Model):
    pass


    

    


