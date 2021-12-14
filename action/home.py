from owner.models import owners , products  , orders
from users.models import Address
def color (request) :
  req = request.GET
  
  #-----------colour--------------#
 
  c = 'light'
  # data in variable
  dark = req.get ('dark')
  colour = "#1e2526"
  tcolour = "#5eb8cf"
  if dark == 'dark' :
    colour="rgb(24,27,28)"
    tcolour = "#ffffff"
  elif dark == 'light':
    colour ="rgb(235,240,241)"
    tcolour = "#000000"
    c= 'dark'
  #-----------end colour--------------
  #colour--------------
  
  data = {
   'colour' :colour,'c':c,'tcolour':tcolour,
  
    }
  
    
  return data
 
def create (request):
  req = request.GET
  
  #-----------colour--------------#
 
  c = 'light'
  # data in variable
  dark = req.get ('dark')
  colour = "#1e2526"
  tcolour = "#5eb8cf"
  if dark == 'dark' :
    colour="rgb(24,27,28)"
    tcolour = "#ffffff"
  elif dark == 'light':
    colour ="rgb(235,240,241)"
    tcolour = "#000000"
    c= 'dark'
  #-----------end colour--------------
  #colour--------------
  err = 'noerr'
  NAME = []
  name_check = False
  ownerss = owners.objects.all()
  for owner in ownerss:
    NAME = owner.name
    if request.method == 'POST':
      name = request.POST['Name']
      if NAME == name :
        name_check = True
  
  data = {
   'colour' :colour,'c':c,'tcolour':tcolour,'name_check':name_check
  
    }
  
    
  return data
  
def db (request,Name_check):
  datab = False
  
  if request.method == "POST":
    
    name = request.POST['Name']
    email = request.POST['email'] 
    password = request.POST['password']
    phone = request.POST['phone']
    if name == "":
      name = False
    elif password == "":
      password = False
    elif email == "":
      email = False
    else :
      if Name_check == False:
        new_db = owners (
        name = request.POST['Name'],
        email = request.POST['email'], 
        password = request.POST['password'],
        phone = request.POST['phone']
           )
        new_db.save()
        datab = True
  return datab 

def search (request, owner):
  url = False  
  if request.method == "POST":
    #print (request.POST)
    name = request.POST['u_name']
    password = request.POST ['Password']
    for i in owner :
      Name = i.name
      Password = i.password
      
      if name == Name and password == Password:
        url = True
        break
      
  return url
    
def u_name (request):
  if request.method == "POST":
    #print (request.POST)
    name = request.POST['u_name']
    return name
def homep (request,name):
  req = request.GET
  owner = owners.objects.all()
  product = products.objects.all()
  #-----------colour--------------#
 
  c = 'light'
  # data in variable
  dark = req.get ('dark')
  colour = "#1e2526"
  tcolour = "#5eb8cf"
  if dark == 'dark' :
    colour="rgb(24,27,28)"
    tcolour = "#ffffff"
  elif dark == 'light':
    colour ="rgb(235,240,241)"
    tcolour = "#000000"
    c= 'dark'
  
  allProducts = []
  for i in product:
    
    if i.owner_name == name :
      o_product = products.objects.get (id=i.id)
      allProducts.append(o_product)
      
      
      print (o_product.name)
    

      print (o_product)
  data = {
   'colour' :colour,'c':c,'tcolour':tcolour,'oname':name
  ,'ourl':f'/owner/add/{name}',
  'products':product,
  'allProducts':allProducts,
  


  
    }
  return data
  #-----------end colou


def add (request,o_name):
  print (request)
  data = {
    'oname':o_name,'t_f':False,
    }  
  #data = {'oname':o_name}
  if request.method == "POST":
    #print ('hello')
    new_db = products (
      name = request.POST['name'],
      price = request.POST['price'],
      image = request.POST['logo'],
      image2 = request.POST['image2'],
      image3 = request.POST['image3'],
      stock = request.POST['stock'],
      video = request.POST['video'],
      star = request.POST['star'],
      discription = request.POST['discription'],
      discount = request.POST['discount'],
      owner_name = o_name
    )
    new_db.save()
    
    data = {
    'oname':o_name,'t_f':True,
    }  
  return data
def update (request,pk,o_name):
  product = []
  t_f = False
  a = products.objects.get (id=pk)
  product.append (a)
  if request.method == "POST":
    #print ('hello')
    owner = products.objects.get (id=pk)
    owner.delete()
    new_db = products (
      name = request.POST['name'],
      price = request.POST['price'],
      image = request.POST['logo'],
      image2 = request.POST['image2'],
      image3 = request.POST['image3'],
      stock = request.POST['stock'],
      video = request.POST['video'],
      star = request.POST['star'],
      discription = request.POST['discription'],
      discount = request.POST['discount'],
      owner_name = o_name
    )
    new_db.save()
 
    t_f = True
    
  data = {
    'oname':o_name,'t_f':t_f,
    'products':product
    }
  return data
def ohome (request,name):
  req = request.GET
  owner = owners.objects.all()
  product = products.objects.all()
  #-----------colour--------------#
 
  c = 'light'
  # data in variable
  dark = req.get ('dark')
  colour = "#1e2526"
  tcolour = "#5eb8cf"
  if dark == 'dark' :
    colour="rgb(24,27,28)"
    tcolour = "#ffffff"
  elif dark == 'light':
    colour ="rgb(235,240,241)"
    tcolour = "#000000"
    c= 'dark'
  
  allProducts = []
  for i in product:
    
    if i.owner_name == name :
      o_product = products.objects.get (id=i.id)
      allProducts.append(o_product)
      
      
      print (o_product.name)
    

      print (o_product)
  data = {
   'colour' :colour,'c':c,'tcolour':tcolour,'oname':name
  ,'ourl':f'/add/{name}',
  'products':product,
  'allProducts':allProducts


  
    }
  return data
  #-----------end colou
def orderz (request,name,toname):
  order = orders.objects.all()
  produ = []
  address = ''
  for i in order :
    if i.From == name:
      address = Address.objects.get(id=i.data)
      prod = products.objects.get(id=i.pid)
      produ.append(prod)
  data = {
    'orders':order,'address':address,'product':produ,'name': name,'image':'https://wallpapers.com/images/high/splashing-water-gradient-background-mobile-v5hlk4ta55rn5w3x.jpg'
  }
  return data
def contact (request,name):
  img = [1,2,4]
  if request.method == "POST":
    new_db = orders (
      From = "Akhil",
      data = request.POST['data'],
      to = "Akhilesh"
      )
    new_db.save()
  From = []
  order = orders.objects.all()
  for i in order :
    if i.to == "Akhil":
      From1 = orders.objects.get (id=i.id)
      From.append(From1)
    
  data = {
    'orders':order,'img':img,'name':name,'image':'https://wallpapers.com/images/high/splashing-water-gradient-background-mobile-v5hlk4ta55rn5w3x.jpg'
  }
  return data