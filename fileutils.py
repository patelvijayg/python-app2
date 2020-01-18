from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo

# import secrets secrets.token_hex(16)
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


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

@app.route("/file-save",methods=['POST'])
def filesave():
    if 'filename' in request.files:
        actualfile=request.files['filename']
        mongo.save_file(actualfile.filename,actualfile)
        mongo.db.users.insert({'username':request.form.get('username'),'filename':actualfile.filename})
        return "uploaded"

@app.route("/file/<filename>",methods=['GET'])
def fileget(filename):
    return mongo.send_file(filename)


@app.route("/user/<username>", methods=['GET'])
def user(username):
    user=mongo.db.users.find_one({'username':username})
    filename=user['filename']


    text1=mongo.send_file(filename)
    result=f'''
            <h1> {username} </h1>
            <label> {text1} </label>
           '''
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)