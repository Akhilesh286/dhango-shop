from owner.models import owners , products , orders

def home (request):
  product = products.objects.all()
  data = {
   'products':product
  }
  return data