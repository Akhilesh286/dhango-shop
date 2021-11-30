from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ,name = 'index' ),
    path('admin/',views.admin ,name = 'admin' ),
    path ('update/<str:pk>/<str:name>/', views.update),
    
    
    path ('delete/<str:pk>/<str:a_p>/<str:name>',views.delete,name="delete"),
    path ('create/',views.create),
    path ('add/<str:o_name>/',views.add),
    path ('ohome/<str:name>', views.ohome),
    
    #dynamic url
    path ('homep/<str:search>/<str:name>/',views.homep ),
    
    path ('js/',views.js),
    path ('orders/<str:name>/' , views.orders),
    path ('contact/<str:name>/' , views.contact),
    
    
]
