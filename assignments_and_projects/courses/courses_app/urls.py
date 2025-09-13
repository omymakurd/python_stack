from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('add_course',views.add_course,name="add_course"),
    path('show_courses',views.show_courses,name="show_courses"),
    path('courses/destroy/<int:id>',views.show_details,name='show_details'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),

]
