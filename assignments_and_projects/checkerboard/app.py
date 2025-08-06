from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def checker_default():
    return render_template('index.html',width=8,height=8,color1='red',color2='black')
@app.route('/<int:height>')
def checker_height(height):
    return render_template('index.html',width=8,height=height,color1='#556B2f',color2='white')
@app.route('/<int:width>/<int:height>')
def checker_custom(width,height):
    return render_template('index.html',width=width,height=height,color1='red',color2='black')
if __name__=='__main__':
    app.run(debug=True,port=5050)