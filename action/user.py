from owner.models import owners , products , orders
from users.models import users
def home (request):
  product = products.objects.all()
  data = {
   'products':product
  }
  return data
def login (request):
  req = request
  if req.method == "POST":
    name = request.POST['name']
    password = request.POST['password']
    print (name,password)
def create (req):
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
    elif password == '':
      null = False
    elif date == '':
      null = False
    elif email == "":
      null = False
    elif number == '':
      null = False
    elif gender == "":
      null = False
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
      print (name,password,date,email,number,gender)