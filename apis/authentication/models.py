from django.db import models

# Create your models here.

class User_Authentication(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)


class Doctor_Authentication(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)

# class User_Details(models.Model):