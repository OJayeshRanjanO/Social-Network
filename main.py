from flask import Flask,render_template,request,make_response
import json
from database_functions import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    recvJson = request.get_json()
    firstname = recvJson['firstname']
    lastname = recvJson['lastname']
    username = recvJson['username']
    password = recvJson['password']
    fromDB = addUser(username,password,'user',lastname,firstname)
    return str(json.dumps({"signup":"success"})) if fromDB else str(json.dumps({"signup":"failure"}))

@app.route('/login',methods=['POST'])
def login():
    recvJson = request.get_json()
    username = recvJson['username']
    password = recvJson['password']
    fromDB = checkUserPresent(username, password)
    if not fromDB:
        return str(json.dumps({"login":"failure"}))
    else:
        return str(json.dumps({"login": "success","username":username}))

@app.route('/home')
def home():
    # username = recvJson['username']
    # resp = make_response(render_template("home.html"))
    # resp.set_cookie('username', 'admin')
    # return resp
    return render_template("home.html")

@app.route('/createCircle',methods=['POST'])
def createCircle():
    recvJson = request.get_json()
    circle_name = recvJson['circle_name']
    circle_type = recvJson['circle_type']
    username = recvJson['username']
    userid = (getUserID(username))['userid']
    circles = addCircle(circle_name,circle_type,userid)
    return str(json.dumps({"circle_name": circles['circle_name'],'circle_id':circles['circleid']}))

@app.route('/deleteCircle',methods=['POST'])
def deleteCircle():
    recvJson = request.get_json()
    circleid = recvJson['circleid']
    username = recvJson['username']
    removeCircle(circleid)
    return str(json.dumps({"status": 'success'}))


@app.route('/loadPage',methods=['POST'])
def reloadPage():
    recvJson = request.get_json()
    username = recvJson['username']
    userid = (getUserID(username))['userid']
    circleList = getCircles(userid)
    return str(json.dumps({"circle": circleList}))



if __name__ == '__main__':
    app.run(debug=True)