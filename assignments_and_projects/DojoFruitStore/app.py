from flask import Flask,render_template,request,redirect,session,url_for
app=Flask(__name__)
app.secret_key="secret"
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/checkout',methods=['POST'])
def checkout():
    print(request.form)
    strawberry=request.form['strawberry']
    raspberry=request.form['raspberry']
    apple=request.form['apple']
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    student_id=request.form['student_id']
    count=int(strawberry)+int(raspberry)+int(apple)
    customer_name=first_name+" "+ last_name
    print(f"Charging {customer_name} for {count} fruits")
    session['order']={
        'strawberry':strawberry,
        'raspberry':raspberry,
        'apple':apple,
        'first_name':first_name,
        'last_name':last_name,
        'count':count
    }
    return redirect(url_for('checkout_get'))
    #return render_template("checkout.html",strawberry=strawberry,raspberry=raspberry,apple=apple,first_name=first_name,last_name=last_name,student_id=student_id,count=count)
@app.route('/checkout')
def checkout_get():
    order=session.get('order',None)
    if order:
        return render_template("checkout.html",**order)
    return redirect('/')
@app.route('/fruits')
def fruits():
    return render_template("fruits.html")
if __name__=='__main__':
    app.run(debug=True,port=5525)
