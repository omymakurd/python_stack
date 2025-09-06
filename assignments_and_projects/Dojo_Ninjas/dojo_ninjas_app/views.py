from django.shortcuts import render,redirect
from .models import Dojos,Ninjas
from django.db.models import Count
def index(request):
    context={
        "dojos":Dojos.objects.annotate(ninjas_count=Count('ninjas'))
    }
    return render(request,"index.html",context)
def add_dojo(request):
    if request.method=='POST':
        name=request.POST['name']
        city=request.POST['city']
        stat=request.POST['stat']
        desc=request.POST['desc']
        Dojos.objects.create(
            name=name,
            city=city,
            stat=stat,
            desc=desc
        )
        return redirect('/')
    return redirect('/')

def add_ninja(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dojo_id=request.POST['dojo']
        dojo=Dojos.objects.get(id=dojo_id)
        Ninjas.objects.create(
            first_name=first_name,
            last_name=last_name,
            dojo=dojo
        )
        return redirect('/')
    return redirect('/')
def delete_dojo(request,dojo_id):
    dojo=Dojos.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('/')

# Create your views here.
