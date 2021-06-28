from flask import Flask, render_template, request
from flask import request
from jarvis_main import *

app = Flask('')
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    update_user('user',request.remote_addr)
    userText = request.args.get('msg')
    return str(reply(userText,request.remote_addr))

run = app.run(debug=False,host='0.0.0.0')
