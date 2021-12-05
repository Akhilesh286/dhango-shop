from django.contrib import admin
from .models import users , Rate , cart ,Favourite
class usersAdmin (admin.ModelAdmin):
  list_display = ('name','password','email','phone','gender','date')
class RateAdmin (admin.ModelAdmin):
  list_display = ['pid','star','id','comment']
class cartAdmin (admin.ModelAdmin):
  list_display = ['pid','uid','id']
class FavouriteAdmin (admin.ModelAdmin):
  list_display = ['uid','pid']
# Register your models here.
admin.site.register(users,usersAdmin)
admin.site.register(Favourite,FavouriteAdmin)
admin.site.register(Rate,RateAdmin)
admin.site.register(cart,cartAdmin)  