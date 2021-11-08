from django.db import models

class owners (models.Model):
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=10)
  items  = models.IntegerField()
# Create your models here.
class Product (models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField()
  stock = models.IntegerField()
  image = models.CharField(max_length=2500)