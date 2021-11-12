from django.shortcuts import render , redirect
from .models import Todo

def index (request):
  todo = Todo.objects.all()
  if request.method == "POST":
    new_todo = Todo (
      title = request.POST['title']
      )
    new_todo.save()
    return redirect ('/')
  data = {
    'todos':todo
  }
  return render (request,'index.html',data)
# Create your views here.
def delete (request,pk):
  todo = Todo.objects.get (id=pk)
  
  todo.delete()
  return redirect ('/')