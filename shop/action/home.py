def home (request,products) :
  req = request.GET
  print (products)
  #-----------colour--------------#
 
  c = 'light'
  # data in variable
  dark = req.get ('dark')
  colour = "#1e2526"
  if dark == 'dark' :
    colour="rgb(24,27,28)"
  elif dark == 'light':
    colour ="rgb(235,240,241)"
    c= 'dark'
  #-----------end colour--------------
  data = {
   'colour' :colour,'c':c,
    }
  
    
  return data
    