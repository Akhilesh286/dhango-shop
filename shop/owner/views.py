from django.shortcuts import render
from django.http import HttpResponse
from .models import owners , Product
from action import home , link
# Create your views here.
def index (request):
  
  products = Product.objects.all()
  data = home.login(request,owners)
  url = home.home (request)
  if url == True:
    return render (request,'home.html')
    url = home.home (request)
    
    
  return render (request,'login.html',data)

