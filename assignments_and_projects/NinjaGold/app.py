from flask import Flask,render_template,redirect,request,session
import random
from datetime import datetime
app=Flask(__name__)
app.secret_key="ninja_gold_secret"
@app.route("/")
def  index():
    if "gold" not in session:
        session["gold"]=0
        session["activities"]=[]
        session["moves"]=0
        session["game_over"]=False
    return render_template("index.html",gold=session["gold"],activities=session["activities"],moves=session["moves"],game_over=session["game_over"])
@app.route("/process_money",methods=["POST"])
def process_money():
    if session.get("game_over",False):
        return redirect("/")
    building=request.form["building"]
    session["moves"]+= 1
    ranges={
        "farm":(10,20),
        "cave":(5,10),
        "house":(2,5),
        "casino":(-50,50)
    }
    gold_earned=random.randint(*ranges[building])
    session["gold"]+=gold_earned
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if gold_earned>0:
        activity={
            "text":f"Earned {gold_earned} golds from the {building}! ({time})","class":"gain"
        }
    elif gold_earned <0:
        activity={
            "text":f"Entered a {building} and lost {abs(gold_earned)} golds ... ouch!({time})","class":"loss"
        }
    else:
        activity={
            "text":f"Entered a {building} but neither won nor lost gold.({time})","class":"loss"
        }
    session["activities"].insert(0,activity)
    if session["gold"]>=500 and session["moves"] <=15:
        session["game_over"]=True
        session["activities"].insert(0,{"text":"You won the game!","class":"gain"})
    elif session["moves"]>=15:
        session["game_over"]=True
        session["activities"].insert(0,{"text":"Game over! you lost","class":"loss"})
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True,port=5478)