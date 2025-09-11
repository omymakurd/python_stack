
from django.urls import path,include
from . import views

urlpatterns = [
  
   path('',views.index,name="index"),
   path('register',views.register),
   path('login',views.login),
   path('success',views.success,name="success"),
   path('logout',views.logout,name="logout")
]