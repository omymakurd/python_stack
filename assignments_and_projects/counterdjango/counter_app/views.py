from django.shortcuts import render,redirect
def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    request.session['counter']+= 1
    return render(request,"index.html")
def destroy(request):
    if 'counter' in request.session:
       del request.session['counter']
    return redirect('/')
def add2(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    request.session['counter']+=2
    return render(request,"index.html")
def  addcustome(request):
    if request.method =='POST':
        increment=int(request.POST.get('increment',1))
        if 'counter' not in request.session:
            request.session['counter']=0
        request.session['counter']+= increment
    return render(request,"index.html")
# Create your views here.
