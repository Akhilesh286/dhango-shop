from django.shortcuts import render
from django.http import HttpResponse
from .models import owners , Product
from action import home as h
# Create your views here.
def index (request):
  products = Product.objects.all()
  """
  text1 = request.GET
  name = text1.get ("name")
  text1 = request.GET
  name = text1.get ("name")
  hello = 'hello'
  data = {'products':products,'text':name,'hello':hello}
  """
  data = h.home(request,products)
  return render (request,'home.html',data)