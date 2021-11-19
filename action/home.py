from owner.models import owners , products

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
  if request.method == "POST":
    ownerss = owners.objects.all()
    for owner in ownerss:
      NAME = owner.name
      if request.POST['Name']==NAME:
        err = 'err'
  data = {
   'colour' :colour,'c':c,'tcolour':tcolour,'err':err
  
    }
  
    
  return data
  
def db (request):
  datab = False
  
  if request.method == "POST":
    new_db = owners (
      name = request.POST['Name'],
      email = request.POST['email'], 
      password = request.POST['password'],
      )
    new_db.save()
    datab = True
  return datab 

def search (request, owner):
  url = False  
  if request.method == "POST":
    print (request.POST)
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
    print (request.POST)
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
  for i in product:
    if i.owner_name == name:
      print ('hhhhh')
  data = {
   'colour' :colour,'c':c,'tcolour':tcolour,'j':owner,'oname':name
  ,'ourl':f'/add/{name}',
  
    }
  return data
  #-----------end colou


def add (request,o_name):
  print (request)
  data = {'oname':o_name}
  if request.method == "POST":
    print ('hello')
    new_db = products (
      name = request.POST['name'],
      price = request.POST['price'],
      image = request.POST['logo'],
      image2 = request.POST['image2'],
      image3 = request.POST['image3'],
      image4 = request.POST['image4'],
      image5 = request.POST['image5'],
      stock = request.POST['stock'],
      video = request.POST['video'],
      star = request.POST['star'],
      discription = request.POST['discription'],
      discount = request.POST['discount'],
      owner_name = o_name
    )
    new_db.save()
    
    data = {
    'name':name ,
    'oname':o_name,
    'price':price
    }  
  return data