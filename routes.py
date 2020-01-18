from flask import render_template,  request, session,url_for, flash, redirect
from dashboard import app, mongo
import models

@app.route("/")
def home():
    return render_template('testing.html')

@app.route("/upload",methods=['POST'])
def upload():
    if 'filename' in request.files:
        actualfile=request.files['filename']
        mongo.save_file(actualfile.filename,actualfile)
        mongo.db.users.insert({'username':request.form.get('username'),'filename':actualfile.filename})
        return "uploaded"

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)