from django.shortcuts import render,redirect
def index(request):
    return render(request,"index.html")
def create_user(request):
    name=request.POST['name']
    email=request.POST['email']
    request.session['name']=name
    request.session['email']=email
    

    return render(request,"show.html")

# Create your views here.
