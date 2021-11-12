from owner.models import owners , Product

def search (owners):
  for owner in owners :
    o = owner.name
    print (o)