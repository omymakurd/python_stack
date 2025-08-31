from django.shortcuts import render,redirect
def index(request):
    return render(request,"index.html")
def show_data(request):
    if request.method == "POST":
        name=request.POST['name']
        location=request.POST['location']
        language=request.POST['language']
        comment=request.POST['comment']
        gender=request.POST['gender']
        interests=request.POST['interests']

        context={
            "name":name,
            "location":location,
            "language":language,
            "comment":comment,
            "gender":gender,
            "interests":interests
        }
        return render(request,"show.html",context)
    return redirect('/')
# Create your views here.
