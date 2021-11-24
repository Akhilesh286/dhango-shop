from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ,name = 'index' ),
    path('a/',views.admin ,name = 'admin' ),
    
    
    path ('delete/<str:pk>',views.delete,name="delete"),
    path ('c/',views.create),
    path ('css/',views.css),
    #dynamic url
    path ('b/<str:search>/<str:name>/',views.homep )
    
    
]
