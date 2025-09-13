from django.shortcuts import render,redirect
from courses_app.models import *
from django.contrib import messages 

def index(request):
    context={
        "all_courses":Courses.objects.all()
    }
    return render(request,"index.html",context)
  
def add_course(request):
     if request.method == 'POST':
        errors=Courses.objects.course_validator(request.POST)
       
        if len(errors)>0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('index')
        else:
            course_name=request.POST['course_name']
            desc=request.POST['desc']
            Courses.objects.create(course_name=course_name,desc=desc)
            messages.success(request,"Successfully create Courses")
            return redirect('index')
     return redirect('index')
def show_courses(request):
    context={
        "all_courses":Courses.objects.all()
    }
    return render(request,"index.html",context)
def show_details(request,id):
    course=Courses.objects.get(id=id)
    context={
        "course":course
    }
    return render(request,"delete_course.html",context)

def delete_course(request,id):
    course=Courses.objects.get(id=id)
    course.delete()
    return redirect("index")
# Create your views here.
