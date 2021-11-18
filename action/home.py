from owner.models import owners

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
def homep (request):
  req = request.GET
  owner = owners.objects.all()
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
  data = {
   'colour' :colour,'c':c,'tcolour':tcolour,'j':owner
  
    }
  return data
  #-----------end colou