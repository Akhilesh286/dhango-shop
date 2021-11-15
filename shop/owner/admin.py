from django.contrib import admin
from .models import owners ,products
class ownersAdmin (admin.ModelAdmin):
  list_display = ('name','password','email')
  
 

class productsAdmin (admin.ModelAdmin):
  list_display = ('owner_name','item_name','discount','rate','price','image')

admin.site.register(owners , ownersAdmin) 
admin.site.register(products,productsAdmin)
# Register your models here.
