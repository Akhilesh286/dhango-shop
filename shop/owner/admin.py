from django.contrib import admin
from .models import Product ,owners
class ownersAdmin (admin.ModelAdmin):
  list_display = ('name','password','items')
class ProductAdmin (admin.ModelAdmin):
  list_display = ('name','price','stock','image')


admin.site.register(Product,ProductAdmin)
admin.site.register(owners , ownersAdmin) 
# Register your models here.
