from django.contrib import admin
from .models import users
class usersAdmin (admin.ModelAdmin):
  list_display = ('name','password','email','phone','gender','date')
# Register your models here.
admin.site.register(users,usersAdmin) 