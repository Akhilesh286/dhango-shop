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

def cart (request,uid):
  data = user.cart1(request,uid)
  addr = data.get('addr')
  price = data.get('price')
  qty = data.get ('qty')
  pk = data.get ('pk')
  tf = data.get ('tf')
  
  if tf == True :
    return redirect (f'/buy/{addr}/{price}/{qty}/{pk}/{uid}/')
  return render (request,'cart.html',data)

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

def addcart (request,uid,pid):
  acart = user.acart(request,uid,pid)
  if acart == True :
    return redirect(f'/home/{uid}')
def buy (request,addr,price,qty,pk,uid):
  data = user.buy (request,addr,price,qty,pk,uid)
  return render (request,'buy.html',data)
def address (request,uid):
  data = user.address(request,uid)
  return render (request,'address.html',data)
  
def favourite (request,uid):
  data = user.favourite(request,uid)
  return render (request,'favourite.html',data)