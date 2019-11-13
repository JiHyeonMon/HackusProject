from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null = True)
    nickname = models.TextField(max_length = 18)
    email = models.EmailField(unique=True)