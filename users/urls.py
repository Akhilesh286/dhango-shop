from django.urls import path
from . import views

urlpatterns = [
  path ('',views.home),
  path ('cart/',views.cart),
  path ('login/',views.login),
  path ('create/',views.create)
  ]