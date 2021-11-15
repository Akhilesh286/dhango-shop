from django.db import models

class owners (models.Model):
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=10)
  email = models.CharField(max_length=100)
  


class products (models.Model):
  owner_name = models.CharField(max_length=255),
  item_name = models.CharField(max_length=255),
  discount = models.FloatField(),
  price = models.FloatField(),
  rate = models.FloatField(),
  image = models.CharField(max_length=25000),
  
  
# Create your models here.