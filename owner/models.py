from django.db import models

class owners (models.Model):
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=10)
  email = models.CharField(max_length=100)
  

# Create your models here.
