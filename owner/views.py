from django.shortcuts import render
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import owners , products
from .models import orders as orde
from users.models import users
from action import home 
# Create your views here.
def index (request):
  
  owner=owners.objects.all()
  data = home.color(request)
  search = home.search (request,owner)
  u_name = home.u_name(request)
  if search == True :
    return redirect (f'/owner/homep/True/{u_name}/')
  
    
 
 
  return render (request ,'login.html',data)

def delete (request,pk,a_p,name):
  if a_p == "p":
    product=  products.objects.get (id=pk)
    pname = product.name
    data = {
      'pname' : pname
    }
    if(request.method=="POST"):
      btn = request.POST['btn1']
      if btn == '0':
        return redirect (f'/owner/homep/True/{name}/')
      else :
        product.delete()
        return redirect (f'/owner/homep/True/{name}/')
  return render (request,'del.html',data)

def admin1 (request):
  owner=owners.objects.all()
  order = orde.objects.all()
  user = users.objects.all()
  product = products.objects.all()
  data = {
    'owners':owner,
    'order':order,
    'user':user,
    'product':product
  }
  return render (request,'admin.html',data)
def admin (request):
  if request.method == "POST":
    name = request.POST['name']
    password = request.POST['password']
    if name == "Akhilesh" and password == "hanuman":
      return redirect ('/owner/admin')
  owner=owners.objects.all()
  order = orde.objects.all()
  user = users.objects.all()
  product = products.objects.all()
  data = {
    'owners':owner,
    'order':order,
    'user':user,
    'product':product
  }
  return render (request,'adminlogin.html',data)
  
  
def create (request):
  data = home.create (request)
  Name_check = data.get('name_check')
  db = home.db (request,Name_check)

  
  
  #print (data)
  if db == True:
    return redirect ('/owner/')
  
  else :
    return render (request,'create.html', data)
  return render (request,'create.html', data)

def homep (request,search,name):
  data = home.homep(request,name)
  #print (search,name)
  return render (request,'home.html',data)
# Create your views here.
def js (request):
  return render (request,'js.html',
  {
    'co':'#f83636'
  })
  
 

def add (request,o_name):
  data = home.add(request,o_name)
  t_f = data.get('t_f')
  if t_f == True:
    return redirect (f'/owner/homep/True/{o_name}')
  print(data)
  return render (request,'add.html',data)
  
  

def update (request,pk,name):
  data = home.update(request,pk,name)
  t_f = data.get('t_f')
  if t_f == True:
    return redirect (f'/owner/homep/True/{name}')
  print(data)
  #return render (request,'add.html',data)
  return render (request,'update.html',data)

def ohome (request,name):
  data = home.ohome(request,name)
  return render (request,'ohome.html',data)
def orders (request,name,toname):
  data = home.orderz(request,name,toname)
  return render (request,'orders.html',data)
def contact (request,name):
  data = home.contact(request,name)
  return render (request,'contact.html',data)