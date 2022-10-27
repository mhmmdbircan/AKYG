from flask import Flask,jsonify,request,make_response,url_for,redirect
from data import fruits

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"


# Get all fruits
@app.route("/fruit")
def allFruits():
    return jsonify(fruits)
