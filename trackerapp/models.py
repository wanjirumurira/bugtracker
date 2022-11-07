from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
#AbstractUser: Use this option if you are happy with the existing fields on the 
# User model and just want to remove the username field.

# Create your models here.
class CustomUserManager(BaseUserManager):
    '''The model managers is a major tool of Django’s ORM that developers use to interact with the database.
    at least one Manager exists for every model in a Django application. 
    Django by default adds the objects manager to every model that is created in the application. 
    add a custom Manager, by subclassing BaseUserManager, that uses an email as the unique identifier instead of a username
    '''
    def create_user(self, email,password,username, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,username=username)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, username, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)    

class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    


