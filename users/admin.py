from django.contrib import admin
from .models import users , Rate
class usersAdmin (admin.ModelAdmin):
  list_display = ('name','password','email','phone','gender','date')
class RateAdmin (admin.ModelAdmin):
  list_display = ['pid','star','id','comment']
# Register your models here.
admin.site.register(users,usersAdmin) 
admin.site.register(Rate,RateAdmin)