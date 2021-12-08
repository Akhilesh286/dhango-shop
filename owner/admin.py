from django.contrib import admin
from .models import owners , orders
class ownersAdmin (admin.ModelAdmin):
  list_display = ('name','password','email')
  
class ordersAdmin (admin.ModelAdmin):
  list_display = ('pid','From','to','data')
  
# Register your models here.
admin.site.register(owners , ownersAdmin) 
admin.site.register(orders, ordersAdmin)
