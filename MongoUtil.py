import pymongo
from pymongo import MongoClient
import json
from bson import json_util
from datetime import datetime

#myclient = MongoClient("mongodb://mongodb2:mongodb2@localhost:27017/sampledb")
#myclient = MongoClient(host='localhost',port=27017,username='mongodb',password='mongodb',authSource='sampledb',authMechanism='SCRAM-SHA-1')
#myclient = MongoClient('ds121753.mlab.com',username='mongodb',password='mongodb2',authSource='sampledb',authMechanism='SCRAM-SHA-256')


URL="mongodb://localhost:27017/"
DATABASE="sampledb"
USER_COLLECTION="userdata"
SENSOR_DATA_COLLECTION="senserdata"
EQUIPMENT_COLLECTION="equipment"

client = MongoClient(URL)
db = client[DATABASE]

def createCollections():
    #mycol1=db[USER_COLLECTION]
    #mycol1=db[SENSOR_DATA_COLLECTION]
    mycol1=db.create_collection(EQUIPMENT_COLLECTION)

def getSensorData(criteria=None):
    _criteria= {} if criteria == None  else criteria
    return db[SENSOR_DATA_COLLECTION].find(_criteria)

def addSensorData(doc,isBulk=False):
    if isBulk:
        db[SENSOR_DATA_COLLECTION].insert_many(doc)
    else:
        db[SENSOR_DATA_COLLECTION].insert_one(doc)

def getUserData(criteria=None):
    result={}
    if criteria == None:
        doc =db[USER_COLLECTION].find({}, {'_id': False})
    else:
        doc =db[USER_COLLECTION].find_one(criteria, {'_id': False})
    return convertToJson(doc)

def addUserData(doc):
    doc["created"]=datetime.now()
    doc["modified"]=datetime.now()
    print(doc)
    result=db[USER_COLLECTION].insert_one(doc)
    return result.inserted_id

def deleteUserData(doc):
    print(doc)
    result=db[USER_COLLECTION].delete_one(doc)
    return result.deleted_count

def updateUserData(username,doc):
    print(doc)
    doc["modified"]=datetime.now()
    updatedoc= { "$set": doc}
    result=db[USER_COLLECTION].update_one({"user":username},updatedoc)
    return result.modified_count

def convertToJson(doc):
    if isinstance(doc,dict):
        return  json.loads(json.dumps(doc,default=str ))
    else:
        result=[]
        for x in doc:
            result.append(json.loads(json.dumps(x,default=str )))
        return {"items": result}