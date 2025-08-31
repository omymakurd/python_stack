from django.urls import path
from . import views
from display_app.views import index
urlpatterns=[
    path('', views.index,name='home'),
    path('time_display/',views.index,name='time_display')
]