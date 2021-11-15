from owner.models import owners

def search (owners):
  for owner in owners :
    o = owner.name
    print (o)