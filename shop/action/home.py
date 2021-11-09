def home (request,products) :
  text1 = request.GET
  name = text1.get ("name")
  print (products)
  c = text1.get ('c')
  h = 'bbb'
  if c=='c':
    h = "aaaaa"
  hello = 'hello'
  if name == "a":
    hello= ' hai'
  hanuman = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4pd-YZx4-hboAHx8a8vKSFJfiIHvyxp2njA&usqp=CAU'
  data = {'products':products,'text':name,'hello':hello , 'image': hanuman,'h':h }
    
  return data
    