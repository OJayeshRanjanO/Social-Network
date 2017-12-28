from flask import Flask,render_template,request
import json
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='root',
                             db='social_network',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    query = "INSERT INTO userdata (username,password) VALUES (%s,%s)"
    connection.cursor().execute(query,('User1','Password1'))
    connection.commit()
finally:
    connection.close()
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template("HEY")
#
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)