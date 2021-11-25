from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ,name = 'index' ),
    path('a/',views.admin ,name = 'admin' ),
    path ('update/<str:pk>/<str:name>/', views.update),
    
    
    path ('delete/<str:pk>/<str:a_p>/<str:name>',views.delete,name="delete"),
    path ('c/',views.create),
    path ('add/<str:o_name>/',views.add),

    #dynamic url
    path ('b/<str:search>/<str:name>/',views.homep ),
    
    path ('js/',views.js)
    
    
]
