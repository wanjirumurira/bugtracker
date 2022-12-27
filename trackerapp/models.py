from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

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

class CreateIssue(models.Model):
    status_choice = (('New', 'New'),
              ('In Progress', 'In Progress'),
              ('Fixed', 'Fixed'),
              ('Closed', 'Closed'),
              ('Reopened', 'Reopened'))

    priority_choice = (('Low Severity', 'Low'),
               ('Medium Severity', 'Medium '),
               ('High Severity', 'High'),
              )
    issue_name = models.CharField(max_length=150)
    issue_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    issue_description = models.TextField(blank=True)
    issue_image = models.ImageField(upload_to="screenshorts",default="default-bug.jpg", null=True)
    created_by = models.CharField(max_length=150)
    assigned_to = models.ManyToManyField(User)
    issue_status = models.CharField(choices = status_choice, max_length=150, default='New')
    issue_severity = models.CharField(choices = priority_choice, max_length=150, default='High')

    def __str__(self):
        return self.issue_name


    


    

    


