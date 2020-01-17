from flask import Flask,request,jsonify
import os
import MongoUtil
import json
app = Flask(__name__)
from recieveCommPort import ReceiveCommPort
import serial


OUTPUT=None

@app.route('/start',methods=['GET'])
def startreading():
    global OUTPUT
    if OUTPUT is None:
        OUTPUT = ReceiveCommPort("COM3", 9600, 0, serial.PARITY_NONE, 1)
    OUTPUT.start()
    OUTPUT.start_reading()
    return "start"

@app.route('/stop',methods=['GET'])
def stopreading():
    global OUTPUT
    OUTPUT.stop_reading()
    OUTPUT.destroy()
    OUTPUT=None
    return "stop"

@app.route('/')
def status():
  return jsonify({"Server":"Running"}),203


@app.route("/create-collections", methods=['POST'])
def createDB():
    MongoUtil.createCollections()
    return "collection create",201

@app.route("/users", methods=['GET', 'POST'])
def userAll():
    if request.method == 'GET':
        result=MongoUtil.getUserData()
        return jsonify(MongoUtil.getUserData())
    elif request.method == 'POST':
        doc = request.data.decode()
        id=MongoUtil.addUserData(json.loads(doc))
        return jsonify(id),201

@app.route("/users/<string:userName>", methods=['GET', 'PUT','DELETE'])
def user(userName):

     if request.method == 'GET':
        if userName != None:
            result =MongoUtil.getUserData({"user":userName})
            print(result)
            return MongoUtil.getUserData({"user":userName})
        else:
            return MongoUtil.getUserData()
     elif request.method == 'PUT':
         doc = request.data.decode()
         id = MongoUtil.updateUserData(userName,json.loads(doc))
         return jsonify(id), 201
     elif request.method == 'DELETE':
         doc = request.data.decode()
         id = MongoUtil.deleteUserData(json.loads(doc))
         return jsonify(id), 201
     else:
      return "Invalid Operation"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

