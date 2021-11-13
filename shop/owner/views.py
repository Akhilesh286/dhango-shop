from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import owners , Product
from action import home , link , search
# Create your views here.
def index (request):
  
  owner=owners.objects.all()
  data = home.color(request)
  search = home.search (request,owner)
  if search == True :
    return redirect ('http://127.0.0.1:8000/b/True')
  
    
 
 
  return render (request ,'login.html',data)

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

def homep (request,pk):
  s = pk
  print ('hh')
  if s =='True':
    return HttpResponse ('hello')
  else :
    return HttpResponse ('hh')
  return HttpResponse ('home')
