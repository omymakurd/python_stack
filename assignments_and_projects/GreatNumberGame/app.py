from flask import Flask,render_template,redirect,request,session
import random
app=Flask(__name__)
app.secret_key='secret_key'
@app.route('/')
def index():
    if 'randomnumber' not in session:
        session['randomnumber']= random.randint(1,100)
        session['attempts']=5
    return render_template("index.html",)
@app.route('/guess',methods=['POST'])
def guess():
    if 'randomnumber' not in session or 'attempts' not in session:
        return redirect('/')
    guess=int(request.form['guess'])
    randomnumber=session['randomnumber']
    session['attempts']-=1
    if guess <randomnumber:
        message=f"Too low! Attempts left:{session['attempts']}"
    elif guess>randomnumber:
        message=f"Too high! Attempts left:{session['attempts']}"
    else:
        message = "correct"
    if session['attempts']<=0 and message != "correct":
        message= f"Game Over! the namber was{randomnumber}"
    return render_template("index.html",message=message)
@app.route('/reset')
def reset():
    session.pop('randomnumber',None)
    session.pop('attempts',None)
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True,port=5369)