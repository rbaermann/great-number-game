from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    session['number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess-again')
def guessAgain():
    if session['answer'] == 'Correct':
        color = 'green'
    else:
        color = 'red'
    return render_template('index.html', answer = session['answer'], color = color)

@app.route('/guess', methods=['POST'])
def guess():
    if session['number'] == int(request.form['number']):
        session['answer'] = 'Correct'
    elif session['number'] > int(request.form['number']):
        session['answer'] = 'Too Low'
    else:
        session['answer'] = 'Too High'
    return redirect('/guess-again')

if __name__ == '__main__':
    app.run(debug=True)