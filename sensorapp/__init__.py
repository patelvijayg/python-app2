from flask import Flask
from flask_pymongo import PyMongo

URL = "mongodb://localhost:27017"
DATABASE = "sampledb"
MONGODB_URL = URL + "/" + DATABASE

USER_COLLECTION = "userdata"
SENSOR_DATA_COLLECTION = "senserdata"
EQUIPMENT_COLLECTION = "equipment"

app = Flask(__name__,template_folder="./templates")

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["MONGO_URI"] = MONGODB_URL
#app.config['DEBUG'] = True

mongo = PyMongo(app)
