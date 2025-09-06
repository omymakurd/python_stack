from django.shortcuts import render,redirect
from .models import Movies
def index(request):
    context={
        "all_the_movies":Movies.objects.all()
    }
    return render(request,"index.html",context)
def adduser(request):
    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        relese_data=request.POST['relese_data']
        duration=request.POST['duration']

        Movies.objects.create(title=title,description=description,relese_data=relese_data,duration=duration)
        return redirect('/')
    return redirect
# Create your views here.
