def home (request,products) :
  text1 = request.GET
  name = text1.get ("name")
  print (products)
  hello = 'hello'
  if name == "a":
    hello= ' hai'
    
  data = {'products':products,'text':name,'hello':hello}
  return data
    