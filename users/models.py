from django.db import models

# Create your models here.
class users (models.Model):
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=10)
  email = models.CharField(max_length=100)
  phone = models.IntegerField()
  date = models.DateField()
  gender = models.CharField(max_length=50)
class Rate (models.Model):
  pid = models.IntegerField()
  comment = models.CharField(max_length=25000)
  star = models.FloatField()

class cart (models.Model):
  pid = models.IntegerField()
  uid = models.IntegerField()
class Address (models.Model):
  uid = models.IntegerField()
  address = models.CharField(max_length=25000)
  number = models.IntegerField()
  name = models.CharField(max_length=250)
  