from sensorapp import mongo,app
import datetime
import json
from flask import Flask, render_template, url_for, request, session, redirect
USER_COLLECTION = "userdata"
SENSOR_DATA_COLLECTION = "senserdata"
EQUIPMENT_COLLECTION = "equipment"

users = mongo.db[USER_COLLECTION]

def validate(user,password):
    if user == 'admin' and password =='password':
        return True
    else:
        return False


def addUserData(doc):
    q={"user":doc['user']}
    u=users.find_one(q)
    doc["modified"] =datetime.datetime.now()
    id=0
    if u is None:
        print(doc)
        doc["created"] = datetime.datetime.now()
        result = users.insert_one(doc)
        id=result.inserted_id
    else:
        updatedoc = {"$set": doc}
        result=users.update_one(q,updatedoc)
        id=result.modified_count
    return id