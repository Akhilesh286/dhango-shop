def login (request,products) :
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
   'colour' :colour,'c':c,'tcolour':tcolour
    }
  
    
  return data
 
def urls (url):
  print (url)
  
def home (request):
  
  
  req = request.GET
  name = req.get ('name')
  password = req.get ('password')
  print (name,password)
  url = False
  if name == "a" and password == 'a':
    url = True
    urls (url)
  return url


