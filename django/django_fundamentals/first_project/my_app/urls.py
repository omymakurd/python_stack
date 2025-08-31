from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('hello/<str:name>/' , views.say_hello,name='say_hello'),
    path('article/<int:id>/', views.article_detail,name='article_detail')
]