from django.shortcuts import render,redirect
from login_app.models import *
from django.contrib import messages
import bcrypt 

def index(request):
    return render(request,"index.html")
def register(request):
    
    if request.method == 'POST':
        errors=User.objects.user_validator(request.POST)
       
        if len(errors)>0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('index')
        else:
            password = request.POST.get('password')
            pw_hash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            birthday=request.POST['birthday']
            if birthday:
               User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash,birthday=birthday)
            else:
                User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash)
            request.session['first_name']=request.POST['first_name']
            messages.success(request,"Successfully create User")
            return redirect('index')
    return redirect('index')
def login(request):
   
    if request.method== 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email).first()
        if user and bcrypt.checkpw(password.encode(),user.password.encode()):
            request.session['first_name']=user.first_name
            messages.success(request,"Successfully logged in")
            return redirect('success')
        else:
            messages.error(request,"Invalid email or password")
            return redirect('index')
def success(request):
     if 'first_name' not in request.session:
        return redirect('index')
     return render(request,"success.html")
def logout(request):
    request.session.flush()
    list(messages.get_messages(request))
    messages.success(request,"You have been logged out")
    return redirect('index')






    
# Create your views here.
