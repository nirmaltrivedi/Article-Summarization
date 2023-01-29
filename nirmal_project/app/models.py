from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RegisterForm(models.Model):

    username = models.CharField(max_length=150,null=False)
    email = models.EmailField(null=False)
    password1 = models.CharField(max_length=150,null=False)
    password2 = models.CharField(max_length=150,null=False)
    occupation = models.CharField(max_length=150,null=False)
    organization = models.CharField(max_length=150,null=False)

    def __str__(self):
        return self.username

class LoginForm(models.Model):

    email = models.EmailField(max_length=150,null=False)
    password = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.email

class Article(models.Model):

    title = models.CharField(max_length=150, null=False)
    url = models.CharField(max_length=150, null=False)
    content = models.TextField(null=False)
    summary = models.TextField(null=False)

    def __str__(self):
        return self.title