from django.db import models

# Create your models here.
class users (models.Model):
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=10)
  email = models.CharField(max_length=100)
  phone = models.IntegerField()
  date = models.DateField()
  gender = models.CharField(max_length=50)