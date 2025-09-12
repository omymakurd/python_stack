from django.shortcuts import render,redirect
from the_wall_app.models import *
import bcrypt
from django.contrib import messages 
from django.utils import timezone
from datetime import timedelta

# Create your views here.
def login(request):
    return render(request,"login.html")
def create_user(request):
    
    if request.method == 'POST':
        errors=Users.objects.user_validator(request.POST)
       
        if len(errors)>0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('login')
        else:
            password = request.POST.get('password')
            pw_hash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            birthday=request.POST['birthday']
            if birthday:
               user=Users.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash,birthday=birthday)
            else:
               user= Users.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash)
            request.session['first_name']=request.POST['first_name']
            request.session['user_id']=user.id
            messages.success(request,"Successfully create User")
            return redirect('login')
    return redirect('login')
def log_in(request):
   
    if request.method== 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=Users.objects.filter(email=email).first()
        if user and bcrypt.checkpw(password.encode(),user.password.encode()):
            request.session['first_name']=user.first_name
            request.session['user_id']=user.id
            messages.success(request,"Successfully logged in")
            return redirect('index')
        else:
            messages.error(request,"Invalid email or password")
            return redirect('login')
    return render(request, "login.html")
def index(request):
    if 'first_name' not in request.session:
        return redirect('login')
    user = Users.objects.get(id=request.session['user_id'])
    all_messages = Messages.objects.all().order_by('-created_at')
    all_comment=Comments.objects.all().order_by('-created_at')

    context = {
        "user": user,
        "all_messages": all_messages,
        "all_comment":all_comment,
    }
    return render(request,"index.html",context)
def logout(request):
    request.session.flush()
    list(messages.get_messages(request))
    messages.success(request,"You have been logged out")
    return redirect('login')
def  create_message(request):
     if request.method=='POST':
        errors=Messages.objects.message_validator(request.POST)
       
        if len(errors)>0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('index')
        else:
            user_id=request.session.get('user_id')
            if not user_id:
                 messages.error(request,"You must be logged in to post a message")
                 return redirect('login')

            message = request.POST.get('message')
            user=Users.objects.get(id=user_id)
            Messages.objects.create(message=message,user=user)
            messages.success(request,"Successfully Add message")
            return redirect('index')
     return redirect('login')
def show_messages(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user=Users.objects.get(id=request.session['user_id'])
    all_messages = Messages.objects.all().order_by('-created_at')
    context={
        "user":user,
        "all_messages":all_messages,
        
    }
    return render(request,"index.html",context)
def add_comment(request,msg_id):
    if request.method=='POST':
        errors=Comments.objects.comment_validator(request.POST)
       
        if len(errors)>0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('index')
        else:
            user_id=request.session.get('user_id')
            if not user_id:
                 messages.error(request,"You must be logged in to add comment")
                 return redirect('login')

            comment = request.POST.get('comment')
            user=Users.objects.get(id=user_id)
            message=Messages.objects.get(id=msg_id)
            Comments.objects.create(comment=comment,user=user,message=message)
            messages.success(request,"Successfully Add Comment")
            return redirect('index')
    return redirect('login')
def show_comment(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user=Users.objects.get(id=request.session['user_id'])
    all_comment = Comments.objects.all().order_by('-created_at')
    all_messages = Messages.objects.all().order_by('-created_at')
    
    context={
        "user":user,
        "all_comment":all_comment ,
        "all_messages":all_messages,
    }
    return render(request,"index.html",context)
def delete_message(request, msg_id):
    if 'user_id' not in request.session:
        return redirect('login')

    message = Messages.objects.get(id=msg_id)
     
    if message.user_id != request.session['user_id']:
        messages.error(request, "You cannot delete this message")
        return redirect('index')
    time_limit=timezone.now() - timedelta(minutes=30)
    if message.created_at < time_limit:
        messages.error(request, "You can only delete your message within 30 minutes of posting")
        return redirect('index')
    message.delete()
    messages.success(request, "Message deleted successfully")

    return redirect('index')
