from owner.models import owners , products , orders

import time

from users.models import users , Rate , cart , Address , Favourite
def home (request):
  product = products.objects.all()
  data = {
   'products':product
  }
  return data
def login (request):
  req = request
  user = users.objects.all()
  
  if req.method == "POST":
    logt = False
    name = request.POST['name']
    password = request.POST['password']
    for i in user :
      if i.name == name and i.password == password :
        logt = True
    return logt
      
def create (req):
  user = users.objects.all()
  if req.method == "POST":
    namecheck = True
    name = req.POST['name']
    for i in user :
      Name = i.name
      if Name == name :
        namecheck = False
    return namecheck
def db (req,namecheck):
  print (namecheck)
  user = users.objects.all()
  if namecheck == True :
    if req.method == "POST":
      name = req.POST['name']
      password = req.POST['password']
      date = req.POST['date']
      email = req.POST['email']
      number = req.POST['number']
      gender = req.POST['flexRadioDefault']
      null = False
      if name == '':
        null = False
        time.sleep(4)
      elif password == '':
        null = False
        time.sleep(4)
      elif date == '':
        null = False
        time.sleep(4)
      elif email == "":
        null = False
        time.sleep(4)
      elif number == '':
        null = False
        time.sleep(4)
      elif gender == "":
        null = False
        time.sleep(4)
      else :
        new_db = users (
          name = name,
          password = password,
          email = email,
          date =date,
          phone = number,
          gender = gender
          )
        new_db.save()
        null = True
      return null
def uname (req):
  if req.method == "POST" :
    name = req.POST['name']
    uname1 = users.objects.get(name=name)
    uid = uname1.id
    return uid
def homep (req,pk):
  if req.method == 'POST':
    uid = req.POST ['uid']
    pid = req.POST['pid']
    print (uid)
    new_db = Favourite (
      uid = uid ,
      pid = pid
      )
    new_db.save()
  fav = Favourite.objects.all()
  
  product = products.objects.all()
  carts = cart.objects.all()
  data = {
   'products':product,
   'uid':pk,
   'fav':fav,
  }
  return data
def rate (req,pk):
  product = products.objects.get (id=pk)
  if req.method == "POST":
    comment = req.POST['comments']
    star = req.POST['star']
    print (comment,star)
    new_db = Rate (
      comment = comment,
      pid = product.id,
      star = star,
      )
    new_db.save()
  pk = int(pk)
  rate = Rate.objects.all()
  product = products.objects.get (id=pk)
  rates = []
  for i in rate :
    if i.pid == pk :
      Rate1 = Rate.objects.get(id=i.id)
      rates.append(Rate1)
  data = {
    'rate':rates
  }
  return data

def acart (req,uid,pid):
  
  new_db = cart(
    pid = pid ,
    uid = uid
    )
  new_db.save()
  return True
def cart1 (req,uid):
  addr1 = ''
  price = ''
  qty = ''
  pk = ''
  tf = False
  uid = int(uid)
  carts =  cart.objects.all()
  cartS = []
  for i in carts :
    if i.uid == uid :
      cart1 = cart.objects.get(id=i.id)
      cartS.append(cart1)
      
  product1 = []
  for i in cartS :
    product = products.objects.get (id=i.pid)
    product1.append(product)
  address = Address.objects.all()
  address3 = []
  for i in address:
    if i.uid == uid :
      address2 = Address.objects.get(id=i.id)
      address3.append(address2)
  if req.method == 'POST':
    addr = req.POST['addr']
    qty = req.POST['qty']
    price = req.POST['price']
    pk = req.POST['pk']
    qty = float (qty)
    price = float (price)
    tf = True
    addr1 = addr
    price = price
    qty = qty
    pk = pk
  
  data = {
    'products':product1,
    'address':address3,
    'addr':addr1,
    'price':price,
    'qty':qty,
    'pk':pk,
    'tf':tf,
  }
  return data
def buy (req,addr,price,qty,pk,uid):
  if req.method == "POST":
    addr = req.POST['addr']
    pid = req.POST['pid']
    to = products.objects.get(id=pid)
    
    new_db = orders (
      to = to.owner_name ,
      From = uid ,
      data = addr
      )
    new_db.save()
  address = Address.objects.get(id=addr)
  pk = int (pk)
  qty = float (qty)
  price = float (price)
  price1 = price*qty
  product = products.objects.get(id=pk)
  data = {
    'price':price,
    'address':address,
    'product':product
  }
  return data
  
def address (req,uid):
  uid = int (uid)
  if req.method == "POST":
    name = req.POST['name']
    address = req.POST['address']
    number = req.POST['number']
    new_db = Address (
      uid = uid ,
      name = name ,
      number = number,
      address = address
      )
    new_db.save()
  Address1 = []
  address = Address.objects.all()
  for i in address:
    if i.uid == uid:
      address1 = Address.objects.get(id=i.id)
      Address1.append(address1)
  data = {
    'address':Address1
  }
  return data

def favourite (req,uid):
  uid = int (uid)
  favourite = Favourite.objects.all()
  products = []
  for i in favourite:
    if i.uid == uid:
      product = Favourite.objects.get (id =i.id)
      products.append(product)
  data = {
    'products':products
  }
  return data