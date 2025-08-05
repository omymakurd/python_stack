from flask import Flask,render_template
app=Flask(__name__)
@app.route('/play')
def level1():
    return render_template('index.html',times=3,color='blue')
@app.route('/play/<x>')
def level2(x):
    return render_template('index.html',times=int(x),color='blue')
@app.route('/play/<x>/<col>')
def level3(x,col):
    return render_template('index.html',times=int(x),color=str(col))
if __name__== '__main__':
    app.run(debug=True)