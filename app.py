from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form['disable']:
            os.system("ansible -h")
        elif request.form['enable']:
            os.system("ansible --version")
        return render_template('index.html'
    else:
        return render_template('index.html')
