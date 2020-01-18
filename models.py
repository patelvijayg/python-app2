from dashboard import mongo,app
import datetime
import json
from flask import Flask, render_template, url_for, request, session, redirect
USER_COLLECTION = "userdata"
SENSOR_DATA_COLLECTION = "senserdata"
EQUIPMENT_COLLECTION = "equipment"

users = mongo.db[USER_COLLECTION]

def addUserData(doc):
    doc["created"] = datetime.now()
    doc["modified"] = datetime.now()
    print(doc)
    result = users.insert_one(doc)
    return result.inserted_id

def uploadUserData(doc):
    doc["created"] = datetime.now()
    doc["modified"] = datetime.now()
    print(doc)
    result = users.insert_one(doc)
    return result.inserted_id

def getUserData(criteria=None):
    result = {}
    if criteria == None:
        doc = users.find({}, {'_id': False})
    else:
        doc = users.find_one(criteria, {'_id': False})
    return convertToJson(doc)


def convertToJson(doc):
    if isinstance(doc, dict):
        return json.loads(json.dumps(doc, default=str))
    else:
        result = []
        for x in doc:
            result.append(json.loads(json.dumps(x, default=str)))
        return {"items": result}
@app.route("/aaa")
def aaa():
    return render_template('photoupload.html')