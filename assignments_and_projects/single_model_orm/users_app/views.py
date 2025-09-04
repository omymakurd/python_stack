from django.shortcuts import render, HttpResponse,redirect
from .models import Users
# Create your views here.
def index(request):
    context={
        "all_users":Users.objects.all()
    }
    return render(request,'index.html',context)
def add_user(request):
    if request.method== 'POST' :
        first_user_name=request.POST['first_name']
        last_user_name=request.POST['last_name']
        email=request.POST['email_address']
        user_age=request.POST['age']
        Users.objects.create(first_name=first_user_name,
                             last_name=last_user_name,
                             email_address=email,
                             age=user_age)
        return redirect('/')
    return redirect('/')