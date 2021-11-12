from owner.models import owners , Product

def login (request,owners) :
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
 
  
def db (request ):
  if request.method == "POST":
    new_db = owners (
      name = request.POST['Name'],
      email = request.POST['email'], 
      password = request.POST['password'],
      )
    new_db.save()


