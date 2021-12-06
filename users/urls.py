from django.urls import path
from . import views

urlpatterns = [
  path ('',views.home),
  path ('cart/<str:uid>/',views.cart),
  path ('login/',views.login),
  path ('create/',views.create),
  path ('home/<str:pk>/',views.homep)
  ,path ('rate/<str:pk>/',views.rate)
  ,path ('contribute/', views.contribute),
  path ('addcart/<str:uid>/<str:pid>/',views.addcart),
  path ('address/<str:uid>/',views.address),
  path ('favourite/<str:uid>/',views.favourite),
  path ('buy/<str:addr>/<str:price>/<str:qty>/<str:pk>/<str:uid>/',views.buy),
  
  ]