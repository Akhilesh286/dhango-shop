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
  return HttpResponse ('hello Cart')

def login (request):
  return HttpResponse ('hello login')

def create (request):
  return HttpResponse ('<h2>hello singup </h1>')