from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return self.username