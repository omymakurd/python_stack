from django.shortcuts import render,redirect
from shows_app.models import *
from django.contrib import messages
def all_shows(request):
    context={
        "shows":Show.objects.all()
    }
    return render (request,"all_show.html",context)
def new_show(request):
    return render(request,"new_show.html")
def add_show(request):
    if request.method == 'POST':
        errors=Show.objects.show_validator(request.POST)
        if len(errors)>0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('new_show')
        else:
           title=request.POST['title']
           network=request.POST['network']
           release_date=request.POST['release_date']
           desc=request.POST['desc']
           Show.objects.create(title=title,network=network,release_date=release_date,desc=desc)
           messages.success(request,"Show created successfuly")
           return redirect('new_show')
    return redirect('new_show')
def show_details(request,id):
    show=Show.objects.get(id=id)
    context={
        "show":show
    }
    return render(request,"show_detail.html",context)
def edit_show(request,id):
    show=Show.objects.get(id=id)
    context={
        "show":show
    }
    return render(request,"edit_show.html",context)
def update_show(request,id):
    if request.method == 'POST':
        errors=Show.objects.show_validator(request.POST)
        if len(errors)>0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('new_show')
        else:
            show=Show.objects.get(id=id)
            show.title=request.POST['title']
            show.network=request.POST['network']
            show.release_date=request.POST['release_date']
            show.desc=request.POST['desc']
            show.save()
            messages.success(request,"Show created successfuly")
            return redirect ('show_details',id=show.id)
    return redirect ('show_details',id=id)
def delete_show(request,id):
    show=Show.objects.get(id=id)
    show.delete()
    return redirect('shows')
# Create your views here.
