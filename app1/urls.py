from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	   
    path('createuser/<int:id>', views.createuser),	
    path('submit', views.submituser),	
    path('logout', views.logout),	
    path('home', views.home, name= "home_route"),	
    path('signup', views.signup),	
    path('create', views.createuser),
    path('myaccount', views.MyAccount),	
    path('createtask', views.createtask),	
    path('createusertask', views.createusertask),	
]