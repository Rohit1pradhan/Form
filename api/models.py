from django.db import models

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    dob=models.CharField(max_length=20)

