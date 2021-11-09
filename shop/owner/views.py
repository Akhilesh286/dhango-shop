from django.shortcuts import render
from django.http import HttpResponse
from .models import owners , Product
from action import home , link
# Create your views here.
def index (request):
  products = Product.objects.all()
  data = home.home(request,products)
  image = link.image ()
  print (image)
  return render (request,'home.html',data)