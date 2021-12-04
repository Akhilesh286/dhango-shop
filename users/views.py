from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , redirect
from owner.models import owners , products
from action import user
from .models import users
# Create your views here.

def home (request):
  data = user.home(request)
  return render (request,'home1.html',data)

def cart (request):
  return render (request,'cart.html')

def login (request):
  data = user.login(request)
  uname = user.uname(request)
  if data == True:
    return redirect (f'/home/{uname}/')
  return render (request,'login1.html')
def create (request):
  namecheck = user.create(request)
  null = user.db(request,namecheck)
  if null == True :
    return redirect ('/login')
  else :
    return render (request,'create1.html',{'nameC':namecheck})
  return render (request,'create1.html',{'nameC':namecheck})
def homep (request,pk):
  data = user.homep(request,pk)
  return render (request,'homep1.html',data)

def contribute (request):
  return render (request,'contribute1.html')

def rate (request,pk):
  data = user.rate(request,pk)
  return render (request,'rate.html',data)