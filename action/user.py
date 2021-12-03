from owner.models import owners , products , orders

import time

from users.models import users
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
  return True