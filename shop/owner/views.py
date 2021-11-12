from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import owners , Product
from action import home , link
# Create your views here.
def index (request):
  owner=owners.objects.all()
  products = Product.objects.all()
  data = home.login(request,owner)
  url = home.db (request)
  print (url)
   
    
    
  return render (request,'login.html',data)

def delete (request,pk):
  owner = owners.objects.get (id=pk)
  
  owner.delete()
  return redirect ('/')

def admin (request):
  owner=owners.objects.all()
  data = {
    'owners':owner
  }
  return render (request,'admin.html',data)
  