from flask import Flask, render_template,request,redirect,session
import random

app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route('/')
def index():
    if not 'counter' in session:
        session['counter'] = 0
    if not 'guess_num' in session:
        session['guess_num'] =0
    if not 'num' in session:
        session['num']= random.randint(1,100)
    print(type(session['counter']),session['counter'])
    print(type(session['guess_num']),session['guess_num'])
    print(type(session['num']),session['num'])
    return render_template("index.html",rnum = session['num'], guess= int(session['guess_num']), count_click= session['counter'])

@app.route('/guess',methods=['POST'])
def guess():
    session['guess_num']=request.form['guess_num']
    session['counter'] +=1
    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/wform',methods=['POST'])
def winnerform():
    session['winner_name']=request.form['winner_name']
    return redirect('/winner')

@app.route('/winner')
def winner():
    if not 'winner_name' in session:
        session['winner_name'] = null
    return render_template("leaderboard.html",wname =session['winner_name'],count_click=session['counter'])

if __name__ == "__main__":
    app.run(debug = True)