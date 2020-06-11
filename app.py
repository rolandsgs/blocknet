from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form['disable']:
            os.system("ansible-playbook -i playbooks/win unblock-internet.yml")
        elif request.form['enable']:
            os.system("ansible-playbook -i playbooks/win block-internet.yml")
        return render_template('index.html'
    else:
        return render_template('index.html')
