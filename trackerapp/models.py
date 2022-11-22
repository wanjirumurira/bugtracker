from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
import uuid
#AbstractUser: Use this option if you are happy with the existing fields on the 
# User model and just want to remove the username field.

# Create your models here.
class CustomUserManager(BaseUserManager):
    '''The model managers is a major tool of Django’s ORM that developers use to interact with the database.
    at least one Manager exists for every model in a Django application. 
    Django by default adds the objects manager to every model that is created in the application. 
    add a custom Manager, by subclassing BaseUserManager, that uses an email as the unique identifier instead of a username
    '''
    def _create_user(self, email, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **extra_fields)
    
    def create_superuser(self, email, username, password=None, **extra_fields):
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
        return self._create_user(email, username, password, **extra_fields)    

class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    username = models.CharField("username", max_length=150,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Project(models.Model):
    project_name = models.CharField(max_length=150,unique=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=True)
    contributors = models.ManyToManyField(CustomUser,related_name="contributors")
    create_at = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.project_name

    

    


