from django.shortcuts import render,HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')")
def say_hello(request,name):
    return HttpResponse(f"hello,{name}")
def article_detail(request,id):
    return HttpResponse(f"this is article number,{id}")
# Create your views here.
