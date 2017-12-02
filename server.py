from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/<word>')
def color(word):
    if word == "blue":
        return render_template("ninjablue.html")



app.run(debug=True)