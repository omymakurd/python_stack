from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result',methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name=request.form['name']
    location=request.form['location']
    language=request.form['language']
    comment=request.form['comment']
    return render_template("show.html",name_on_template=name,location_on_template=location,language_on_template=language,comment_on_template=comment)
if  __name__=='__main__':
    app.run(debug=True)