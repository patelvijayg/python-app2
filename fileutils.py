from flask import Flask, render_template, request
from flask_pymongo import PyMongo

URL="mongodb://localhost:27017"
DATABASE="sampledb"
USER_COLLECTION="userdata"
SENSOR_DATA_COLLECTION="senserdata"
EQUIPMENT_COLLECTION="equipment"

app = Flask(__name__)
#app.config.from_object("application.default_settings")
app.config["MONGO_URI"] = URL+"/"+DATABASE
app.config['MONGO_DBNAME'] = 'mongologinexample'
mongo = PyMongo(app)



@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
        online_users=online_users)

@app.route("/file-save",methods=['POST'])
def filesave():
    if 'filename' in request.files:
        actualfile=request.files['filename']
        mongo.save_file(actualfile.filename,actualfile)
        mongo.db.users.insert({'username':request.form.get('username'),'filepath':actualfile.filename})

if __name__ == '__main__':
    app.run(debug=True)