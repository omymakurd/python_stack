from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.login,name="login"),
    path('create_user',views.create_user,name="create_user"),
    path('login',views.log_in,name="login"),
    path('index',views.index,name="index"),
    path('logout',views.logout,name="logout"),
    path('create_message',views.create_message,name="create_message"),
    path('show_messages',views.show_messages,name="show_messages"),
    path('add_comment/<int:msg_id>',views.add_comment,name="add_comment"),
    path('delete_message/<int:msg_id>',views.delete_message,name="delete_message"),

]
