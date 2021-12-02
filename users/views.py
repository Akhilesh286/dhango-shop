from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , redirect
from owner.models import owners , products
from action import user
# Create your views here.

def home (request):
  data = user.home(request)
  return render (request,'home1.html',data)

def cart (request):
  return render (request,'cart.html')

def login (request):
  data = user.login(request)
  return render (request,'login1.html',data)
def create (request):
  data = user.create(request)
  return render (request,'create1.html')