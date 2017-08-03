from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsMySecret'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/colorValues', methods=['POST'])
def dojoData():
    session['red'] = request.form['red']
    session['green'] = request.form['green']
    session['blue'] = request.form['blue']
    return redirect('/')

app.run(debug=True)
