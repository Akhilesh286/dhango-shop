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
  path ('buy/<str:pk>/',views.buy),
  ]