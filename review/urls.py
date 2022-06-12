from django.urls import path
from . import views

urlpatterns=[
    path('',views.Register, name='register'),  
    path('login/',views.Login, name='login'), 
    path('logout/',views.UserLogout, name='logout'),
   
]
Created profile model and function,set up admin and 