def home (request,products) :
  text1 = request.GET
  name = text1.get ("name")
  print (products)
  colour = text1.get ("colour")
  print (colour)
  button = text1.get ('button')
  buttona= 'button'
  if button=='button':
    buttona = "button action"
  hello = 'hello'
  if name == "a":
    hello= ' hai'
  hanuman = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4pd-YZx4-hboAHx8a8vKSFJfiIHvyxp2njA&usqp=CAU'
  data = {'products':products,'text':name,'hello':hello , 'image': hanuman,'button':buttona ,
    'colour' : colour
  }
    
  return data
    