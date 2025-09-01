from django.shortcuts import render,redirect
import random
leaderboard=[]
def index(request):
    if 'random' not in request.session or 'attempts' not in request.session :
        request.session['random']= random.randint(1,100)
        request.session['attempts']=0
    return render(request,"index.html")
def guess(request):
    user_guess=int(request.POST['guess'])
    request.session['attempts']+=1
    number=request.session['random']
    if request.session['attempts'] > 20 :
        request.session['result']="You Lose! try again"
        return redirect('/')
    if user_guess < number:
        request.session['result']=f"Too Low attemts left : {request.session['attempts']}"
        request.session['color']="red"
    elif user_guess > number:
        request.session['result']=f"Too High! attemts left : {request.session['attempts']} "
        request.session['color']="red"
    else:
        request.session['result']=f"Correct! The number is {request.session['random'] }  you guessed it in {request.session['attempts']} attempts"
        request.session['color']="green"

    return redirect('/')
def reset(request):
    request.session.flush()
    return redirect('/')
def leaderboard_view(request):
    if request.method == "POST":
        name=request.POST['name']
        attempts=request.session.get('attempts',0)
        leaderboard.append({"name":name,"attempts":attempts})
        context={
            "leaderboard":leaderboard
        }
        return render(request,"leaderboard.html",context)
    context={
            "leaderboard":leaderboard
        }
    return render(request,"leaderboard.html",context)

# Create your views here.
