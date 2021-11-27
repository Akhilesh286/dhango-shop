from django.db import models

class owners (models.Model):
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=10)
  email = models.CharField(max_length=100)
  

class products (models.Model):
  owner_name = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  star = models.FloatField()
  image = models.CharField(max_length=2555)
  discription = models.CharField(max_length=255)
  price = models.FloatField ()
  stock = models.FloatField()
  video = models.CharField(max_length=2555)
  discount = models.FloatField()
  image2 = models.CharField(max_length=2555)
  image3 = models.CharField(max_length=2555)
  image4 = models.CharField(max_length=2555)
  image5 = models.CharField(max_length=2555)
  
class orders (models.Model):
  From = models.CharField(max_length=250)
  to = models.CharField(max_length=250)
  data = models.CharField(max_length=50)
  
  
  
  
# Create your models here.
