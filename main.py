from flask import Flask,render_template,request
import json
from database_functions import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    recvJson = request.get_json()
    username = recvJson['username']
    password = recvJson['password']
    fromDB = checkUserPresent(username, password)
    if not fromDB:
        return str(json.dumps({"login":"failure"}))
    else:
        return str(json.dumps({"login": "success"}))



@app.route('/signUp',methods=['POST'])
def signUp():
    recvJson = request.get_json()
    firstname = recvJson['firstname']
    lastname = recvJson['lastname']
    username = recvJson['username']
    password = recvJson['password']
    fromDB = addUser(username,password,'user',lastname,firstname)
    return str(json.dumps({"signup":"success"})) if fromDB else str(json.dumps({"signup":"failure"}))


if __name__ == '__main__':
    app.run(debug=True)