from flask import Flask, render_template,request,redirect,session
import random

app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route('/')
def index():
    if not 'guess_num' in session:
        session['guess_num'] =0
    if not 'num' in session:
        session['num']= random.randint(1,100)
    return render_template("index.html",rnum = int(session['num']), guess= int(session['guess_num']))

@app.route('/guess',methods=['POST'])
def guess():
    session['guess_num']=request.form['guess_num']
    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)