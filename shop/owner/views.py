from django.shortcuts import render
from django.http import HttpResponse
from .models import owners , Product
from action import home , link
# Create your views here.
def index (request):
  global url
  products = Product.objects.all()
  data = home.login(request,products)
  url = home.home (request)
  if url == True:
    return HttpResponse ("<h1>hello </h1>")
    
    
  return render (request,'home.html',data)

