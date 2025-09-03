from django.shortcuts import render,redirect
import random,datetime
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
        request.session['activities']=[]
    return render(request,"index.html")
def process_money(request):
    if request.method == "POST":
        location=request.POST['location']
    gold=0

    if location == 'farm':
         gold=random.randint(10,20)
    elif location == 'cave':
        gold=random.randint(10,20)
    elif location== 'house':
        gold=random.randint(10,20)
    elif location == 'quest':
        gold=random.randint(-50,50)
    request.session['gold']+= gold
    time= datetime.datetime.now().strftime("%B %d %Y %I:%M %p")
    if gold>= 0:
        activity={"text": f"You enterd a {location} and earned {gold} gold. ({time})",
                       "status":"win"
            }
    else :
        activity={ "text":f"You failed a {location} and lost {abs(gold)} gold.({time})",
                      "status":"lose"}
    activities=request.session['activities']
    activities.insert(0,activity)
    request.session['activities']=activities
    return redirect("/")

# Create your views here.
