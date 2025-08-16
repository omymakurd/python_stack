from flask import Flask,render_template,request,redirect,session
app=Flask(__name__)
app.secret_key='secret_key'
@app.route('/')
def index():
    if 'count'  in session:
        session['count']+=1
    else:
       session['count'] =0
    return render_template("index.html",count=session['count'])
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')
@app.route('/add2')
def add2():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return redirect('/')
@app.route('/reset')
def reset():
    session.pop('count',None)
    return redirect('/')
@app.route('/increment',methods=['POST'])
def increment():
    value=request.form.get('value',1,type=int)
    session['count']=session.get('count',0)+value-1
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True,port=5263)