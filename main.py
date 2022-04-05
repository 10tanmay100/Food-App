import pymongo
client = pymongo.MongoClient("mongodb+srv://sap:sap@cluster1.ugtiu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
dataBase = client["Food"]
COLLECTION_NAME = "Food_Products"
collection = dataBase[COLLECTION_NAME]
from flask import Flask, render_template, request,jsonify
# from flask_cors import CORS,cross_origin
import requests
app=Flask(__name__,template_folder='templates')
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")
@app.route("/about",methods=["POST","GET"])
def second():
    l=[]
    if request.method=="POST":
        item=request.form['item']
        calories=request.form['calories']
        qty=request.form['qty']
        record={'item':item,'calories':calories,'qty':qty}
        rec = collection.insert_one(record)
        for i in collection.find():
            l.append(i)
    return render_template("about.html",details=l)
app.run()