from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import subprocess
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    status = {'status':'disconnected'}
    return render_template('index.html', status=status)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/connect", methods=["GET", "POST"])
def connect():

    if request.form.get("status") == "CONECTAR":
        cmd = ["ansible-playbook",
        "-i",
        "/home/rockson/Documentos/developer/blocknet/playbooks/win",
        "/home/rockson/Documentos/developer/blocknet/playbooks/unblock-internet.yml"]

        res = subprocess.check_output(cmd)
        for line in res.splitlines():
            print(line)
        info = {"status" : "success"}
    else:
        cmd = ["ansible-playbook",
        "-i",
        "/home/rockson/Documentos/developer/blocknet/playbooks/win",
        "/home/rockson/Documentos/developer/blocknet/playbooks/block-internet.yml"]

        res = subprocess.check_output(cmd)
        for line in res.splitlines():
            print(line)
        info = {"status" : "success"}
    return jsonify(info)
