from django.contrib import admin
from .models import owners
class ownersAdmin (admin.ModelAdmin):
  list_display = ('name','password','email')
  
 
# Register your models here.
admin.site.register(owners , ownersAdmin) 
