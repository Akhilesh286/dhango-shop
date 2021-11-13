from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import owners , Product
from action import home , link , search
# Create your views here.
def index (request):
  owner=owners.objects.all()
  products = Product.objects.all()
  data = home.color(request)
  
    
  search = home.search (request,owner)
  if search == True :
    return HttpResponse ('hello')
    
    
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
  
  
def create (request):
  data = home.color (request)
  db = home.db (request)
  print (db)
  if db == True:
    return redirect ('/')
  return render (request,'create.html', data)
  